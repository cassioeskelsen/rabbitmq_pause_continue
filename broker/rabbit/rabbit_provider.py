from queue import Empty

from kombu import Connection, Queue, Exchange, Producer, Consumer

from broker.broker_provider import BrokerProvider
from broker.broker_settings import BrokerSettings
from utils.logger import logger
from time import sleep


class RabbitMQProvider(BrokerProvider):
    def __init__(self, broker_configuration: BrokerSettings):
        self.config = broker_configuration
        self.connection = Connection(
            f"amqp://{self.config.get_user()}:{self.config.get_password()}@{self.config.get_host()}:{self.config.get_port()}//"
        )

    def disconnect(self):
        self.connection.close()

    def get_next_message(self, queue_name, max_retry=5):
        with self.connection as _conn:
            sub_queue = _conn.SimpleQueue(queue_name)
            retry_count = 0
            try:
                while True:
                    try:
                        msg = sub_queue.get(block=False, timeout=50)
                        msg.ack()
                        return msg.payload
                    except Empty as e:
                        if retry_count < max_retry:
                            sleep(1)
                            retry_count += 1
                        else:
                            return None
            finally:
                sub_queue.close()

    def declare_queues(self, queues_names):
        with self.connection as _conn:
            _conn.connect()
            channel = _conn.channel()

            for queue_name in queues_names:
                topic = Exchange(
                    name=f"TOPIC/{queue_name}", type="topic", channel=channel
                )
                topic.declare()

                queue = Queue(name=queue_name, channel=channel)
                queue.declare()

                queue.bind_to(exchange=f"TOPIC/{queue_name}")

    def send_message(self, message, topic, routing_key=None):
        with self.connection as _conn:
            _conn.connect()
            channel = _conn.channel()
            producer = Producer(channel)

            logger.info(f"Insert data on TOPIC: {topic}")

            producer.publish(body=message, exchange=topic, routing_key=routing_key)

            logger.info(f"Message {message} sent to topic {topic}!")
