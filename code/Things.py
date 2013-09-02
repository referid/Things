#!/usr/bin/python
# ThingsBase - A database of Things.
import zmq
import riak
import hashlib
import time
import json
import ast

BUCKET = 0
KEY = 1
TAG = 2
ZMQ_SERVER = 'tcp://*:1980'

# Sample JSON Objects
SAMPLE_THING =  {
                'serial':'ABC123',
                'website':'https://acme.com/info',
                'phone':'+18001234567',
                'company':'ACME',
                'manufacture_date':'January 1st, 1970',
                }
SAMPLE_REFERENCE =  {
                    'time':'123456789.101112',
                    'user':'John Doe'
                    }
# Things                
class Things:

  ## Initialize
  def __init__(self):
    try:    
      error = 'Success.'
    except Exception as error:
      pass
    print('[Initializing Things]...' + str(error))

  ## Start ZMQ
  def start_zmq(self): 
    try:    
      context = zmq.Context()
      self.socket = context.socket(zmq.REP)
      self.socket.bind(ZMQ_SERVER)
      error = 'Success.'
    except Exception as error:
      pass
    print('[Starting 0MQ Server]...' + str(error))
  
  ## Start Riak
  def start_riak(self):
    try:
      self.client = riak.RiakClient()
      error = 'Success.'
    except Exception as error:
      pass
    print('[Starting Riak Client]...' + str(error))
  
  ## Listen
  def listen(self):
    try:
      request = json.loads(self.socket.recv())
      error = 'Success.'
    except Exception as error:
      request = None
    print('[Listening]...' + str(error))
    return request

  ## Respond
  def respond(self, response):
    try:
      self.socket.send(json.dumps(response))
      error = 'Success.'
    except Exception as error:
      request = None
    print('[Responding]...' + str(error))

  ## Create new reference to thing after linkwalking, return thing.data
  def get(self, user, company, key):
    company_bucket = self.client.bucket(company)
    thing = company_bucket.get(key)
    links = thing.links
    if links:
      while links:
        print('Link Walking: ' + str(links))
        reference_bucket = self.client.bucket(links[0][BUCKET])
        reference = reference_bucket.get(links[0][KEY])
        links = reference.links
      else:
        print('Reached Last Link...Creating Reference.')
        unix_time = str(int(time.time()))
        reference_bucket = self.client.bucket(unix_time)
        data = {'user':user, 'time':unix_time}
        print(data)
        new = reference_bucket.new(unix_time, data)
        new.store()
        reference.add_link(new)
        reference.store()
    else:
      print('Fresh Thing with no links...Creating Reference.')
      unix_time = str(int(time.time()))
      reference_bucket = self.client.bucket(unix_time)
      reference = reference_bucket.new(unix_time, data = {'user':user, 'time':unix_time})
      reference.store()
      thing.add_link(reference, 'reference')
      thing.store()
    return thing.data

# Main
if __name__ == '__main__':
  test = Things()
  test.start_riak()
  test.start_zmq()
  request = test.listen()
  if (request['type'] == 'GET'):
    response = test.get('Trevor', request['company'], request['serial'])
    test.respond(response)
  else (request['type'] == '
