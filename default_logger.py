#!/usr/bin/env python

import sys
from gcm import GCM

gcm = GCM("API_KEY")
data = {'Message': 'Someone just shutdown your HDFS !!! Its time to check who did it'}


# Send a global notification message. Will be delivered to all subscribers
# Topic Messaging
topic = "global"
gcm.send_topic_message(topic=topic, data=data)
