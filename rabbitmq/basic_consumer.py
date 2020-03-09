#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rabbitmq.rabbit_base import RabbitBase

class BasicConsumerRabbitMQ(RabbitBase):

    def ack_message(self, method):
        self.channel.basic_ack(method.delivery_tag)
    
    def get_next_message(self,  max_retry=5):
        """
        :param max_retry: max attempts to get messages. One second interval between attempts.
        :return: message or None
        """
        from time import sleep

        retry_count = 0

        while True:
            method, property, body = self.channel.basic_get(
                queue=self.QUEUE_NAME, auto_ack=False
            )
            if body:


                return body, method
            else:
                if retry_count < max_retry:
                    sleep(1)
                    retry_count += 1
                else:
                    return None, None
