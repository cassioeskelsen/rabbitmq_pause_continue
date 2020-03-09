#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This code simulates some content producer who is adding information to the queue.
'''
import json
from datetime import datetime
from time import sleep

from rabbitmq.basic_producer import BasicProducerRabbitMQ

if __name__ == '__main__':
    rbmq = BasicProducerRabbitMQ()
    
    while True:
        data = {"date_time": str(datetime.now())}
        rbmq.insert(data, "my_fancy_queue")
        sleep(5)