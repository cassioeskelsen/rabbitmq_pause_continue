#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This code simulates some content producer who is adding information to the queue.
"""
import json
from datetime import datetime
from time import sleep

from broker.broker import Broker

if __name__ == "__main__":
    channels = ["queue1"]
    broker = Broker()
    broker.declare_queues(channels)

    while True:
        data = {"date_time": str(datetime.now())}
        broker.send_message(message=data,  topic="TOPIC/queue1", routing_key=None)
        sleep(5)
