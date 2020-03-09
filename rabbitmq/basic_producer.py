#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from rabbitmq.rabbit_base import RabbitBase

class BasicProducerRabbitMQ(RabbitBase):

    def insert(self, data, queue):
        channel = self.conn.channel()
        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange='', routing_key=queue, body=json.dumps(data))
