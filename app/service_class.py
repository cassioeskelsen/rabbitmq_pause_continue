# -*- coding: utf-8 -*-
import urllib
import json
from utils.logger import logger

class ServiceClass:

    def some_awesome_method_to_deal_with_messages_from_queue_one(self,message):
        logger.info(f"I'm calling a external API to post{message}")
        try:
            query_parameter = message['date_time'].replace(" ","_")
            url = f"http://127.0.0.1:5002/api/whatever_/{query_parameter}"
            f = urllib.request.urlopen(url)
            if f.status == 200:
                return True
            else:
                return False
        except Exception as err:
            logger.error("Can't connect to API")
            return False