#!/usr/bin/python

import zmq
import json
ZMQ_SERVER = 'tcp://127.0.0.1:1980'

# Connect to ZMQ and identifies itself
try:
  context = zmq.Context()
  socket = context.socket(zmq.REQ)
  socket.connect(ZMQ_SERVER)
  error = 'Success.'
except Exception as error:
  pass
print('[Connecting to ZMQ]...' + str(error))

# Send
try:
  request = json.dumps({'type':'GET', 'company':'test', 'serial':'12'})
  socket.send(request)
  error = 'Success.'
except Exception as error:
  pass
print('--> [Sending Request to Server]...' + str(error))
print('\t' + str(request))

# Receive
try:
  response = socket.recv()
  error = 'Success.'
except Exception as error:
  response = None
print('--> [Receiving Response from Server]...' + str(error))
print('\t' + str(response))


