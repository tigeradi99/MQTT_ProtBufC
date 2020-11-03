#!/usr/bin/env python3

import sys
import paho.mqtt.client as paho
import datetime
import example_pb2

# print(sys.version_info)

broker="spr.io"
port=60083
ts = datetime.datetime.now().isoformat()
c = 'client-' + ts[-6:] # use the timestamp to create unique MQTT client
print(c, broker, port)

client= paho.Client(c)
client.connect(broker, port)

# publish an empty string
if len(sys.argv) == 2:
    client.publish(sys.argv[1],'',retain = False, qos=0)
# publish <topic> <message>
elif len(sys.argv) == 3:
    client.publish(sys.argv[1],sys.argv[2],qos=0)
# publish <topic> <message> <retain>
elif len(sys.argv) == 4:
    client.publish(sys.argv[1],sys.argv[2], retain = True, qos=0)
else:
    print(sys.argv[0], '<topic> <message> [True (retain)]')

client.disconnect()
client.loop_stop()
