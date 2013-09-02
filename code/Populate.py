#!/usr/bin/python
# Populate - Fill a bucket with Things.

import riak
import hashlib
import random
import time
import sys

BUCKET = 'test'
NUMBER = int(sys.argv[1])

client = riak.RiakClient()
for val in range(0,NUMBER):
  bucket = client.bucket(BUCKET)
  data = {'serial':val}
  key = str(val)
  thing = bucket.new(key, data)
  thing.store()
  print((BUCKET,key,data))
