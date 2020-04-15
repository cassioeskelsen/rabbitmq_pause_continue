from broker.broker import Broker
from utils.logger import logger


class QueueConsumerWorker:
    def __init__(self):
        self.channels = {"queue1": "method_for_queue1",
                         "queue2": "method_for_queue1"}
        self.broker = Broker()
        self.broker.declare_queues([ele for ele in self.channels])

    def method_for_queue1(self, message):
        try:
            print(message)
            return True
        except:
            return False

    def method_for_queue2(self, message):
        pass

    def run(self) -> bool:
        try:
            for channel, function in self.channels.items():
                message = self.broker.get_next_message(channel)
                if message is not None:
                    if not locals()[function](message):
                        #operation failed, return message to queue
                        self.broker.send_message(message, channel)
            return 0
        except Exception as e:
            logger.error(e, exc_info=True)
            return 1  # return cause
