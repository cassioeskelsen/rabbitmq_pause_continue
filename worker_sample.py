from broker.broker import Broker
from utils.logger import logger


class QueueConsumerWorker:
    def __init__(self):
        self.channels = ["my_fancy_queue"]
        self.broker = Broker()
        self.broker.declare_queues(self.channels)

    def run(self) -> bool:
        try:
            message = self.broker.get_next_message(self.channels[0])
            if message is not None:
                logger.info(f"New message:{message}")
            return 0
        except Exception as e:
            raise e
            logger.error(e, exc_info=True)
            return 1  # return cause
