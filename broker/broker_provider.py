from abc import ABC, abstractmethod


class BrokerProvider(ABC):

    @abstractmethod
    def declare_queues(self, channel_names):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def get_next_message(self, queue_name, max_retry=5):
        pass

    @abstractmethod
    def send_message(self, message, topic, routing_key=None):
        pass
