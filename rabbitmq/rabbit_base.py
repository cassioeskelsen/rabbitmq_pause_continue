#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import pika

class RabbitBase:
    QUEUE_NAME = "my_fancy_queue"
    
    def __init__(self):
        self.conn = self._set_connection()
        self.channel = self.conn.channel()
        self.channel.queue_declare(queue=self.QUEUE_NAME)
        
    def _set_connection(self):
        credentials = pika.PlainCredentials("user", "password")
        parameters = pika.ConnectionParameters(host="localhost", credentials=credentials,
                                               port=5672)
        connection = pika.BlockingConnection(parameters)

        return connection
