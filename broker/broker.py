# -*- coding: utf-8 -*-

from typing import List
from broker.broker_provider_factory import BrokerProviderFactory


class Broker:
    def __init__(self):
        self.broker = BrokerProviderFactory.get_instance()

    def declare_queues(self, queues_names: List):
        self.broker.declare_queues(queues_names)

    def send_message(self, message, topic, routing_key=""):
        self.broker.send_message(message, topic, routing_key)

    def get_next_message(self, channel_name, max_retry=5):
        """
        :param max_retry: max attempts to get messages. One second interval between attempts.
        :return: message or None
        """

        return self.broker.get_next_message(channel_name, max_retry=5)
