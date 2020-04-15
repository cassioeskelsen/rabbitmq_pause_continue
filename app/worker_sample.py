from app.service_class import ServiceClass
from broker.broker import Broker
from utils.logger import logger


class QueueConsumerWorker:
    def __init__(self):
        self.channels = {"queue1": "method_for_queue1",
                         "queue2": "method_for_queue1"}
        self.broker = Broker()
        self.broker.declare_queues([ele for ele in self.channels])

    def method_for_queue1(self,message):
        logger.info(f"called method associate with queue1")
        try:
            return ServiceClass().some_awesome_method_to_deal_with_messages_from_queue_one(message)

        except Exception as e:
            logger.error(f"Some s**t happened")
            return False

    def method_for_queue2(self,message):
        logger.info(f"called method associate with queue2")
        try:
            return ServiceClass().some_awesome_method_to_deal_with_messages_from_queue_one(message)

        except Exception as e:
            logger.error(f"Some s**t happened")
            return False

    def run(self) -> bool:
        try:
            for channel, function in self.channels.items():
                message = self.broker.get_next_message(channel)
                if message is not None:
                    logger.info(f"Queue {channel} - Received message {message}")
                    if not getattr(self, function)(message):
                        self.broker.send_message(message, f"TOPIC/{channel}")
                        #operation failed, return message to queue
                        return 1

            return 0
        except Exception as e:
            logger.error(e, exc_info=True)
            return 1  # return cause
