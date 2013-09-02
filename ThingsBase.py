#!/usr/bin/python
# ThingsBase - A database of Things.
# Headers
import riak
import hashlib
import time
import json
import ast

class ThingsBase:

  def __init__(self, user_name):
    self.client = riak.RiakClient()

  def new_thing(self, serial, user):
    try:
      seconds = int(time.mktime(time.gmtime()))
      key = hashlib.sha224(str(time.time)).hexdigest()
      bucket = self.client.bucket(str(seconds))
      thing = bucket.new(key, data = {'serial':serial, 'user':user})
      thing.store()
      return thing
    except Exception:
      return None

  def get_thing(self, seconds, key):
    try:
      bucket = self.client.bucket(seconds)
      binary = bucket.get(key)
      return binary
    except Exception:
      return None
  
  def new_user(self, user):

if __name__ == '__main__':
  instance = ThingsBase('Trevor')
  thing = instance.new_thing('ABCDEF', 'Trevor')
