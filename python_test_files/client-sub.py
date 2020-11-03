#!/usr/bin/env python3

import queue
import time
import sys
import paho.mqtt.client as paho
import datetime
import random
import example_pb2

# print(sys.version_info)

message_q=queue.Queue()

def empty_queue(delay=0):
    while not message_q.empty():
      m=message_q.get()
      print("Received message  ",m)
    if delay!=0:
      time.sleep(delay)
#define callback
def on_message(client, userdata, message):
   #time.sleep(1)
   now = datetime.datetime.now()
   time_stamp = now.strftime("%m/%d %H:%M:%S")
   print(time_stamp, "receiving <"+ message.topic, end = '>  <')
   print(str(message.payload.decode("utf-8"))+'>')

broker="spr.io"
port=60083
ts = datetime.datetime.now().isoformat()
c = 'client-' + ts[-6:]
print(c, broker, port)
client= paho.Client(c)
client.on_message=on_message

client.connect(broker, port)
if len(sys.argv) == 1:
    client.subscribe("#") # default: subscribe to all topics
else:
    for arg in sys.argv[1:]:
        print("subscribing to ", arg)
        client.subscribe(arg)

client.loop_start() #start loop to process received messages

time.sleep(1)
try:
  while True:
    time.sleep(1)
    pass
except KeyboardInterrupt:
    print ("You hit control-c")

time.sleep(1)

client.disconnect()
client.loop_stop()
