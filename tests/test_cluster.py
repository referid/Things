#!/usr/bin/python
## Test Cluster
import riak
import time

TEST_BUCKET = 'testing'
BUCKET = 0
KEY = 1
VALUE = 2

# Start Client
client = riak.RiakClient()
bucket = client.bucket(TEST_BUCKET)

# First Object
object1 = bucket.new('object1', data = {'created': time.time()})
object1.store()

# Second Object
object2 = bucket.new('object2', data = {'created': time.time()})
object2.store()

# Third Object
object3 = bucket.new('object3', data = {'created': time.time()})
object3.store()

# Link First to Second
object1.add_link(object2)
object1.store()

# Link Second to Third
object2.add_link(object3)
object2.store()

# Link Third to First
object3.add_link(object1)
object3.store()

# Link walk in circles
linksN = object1.links
keyN = linksN[0][KEY]
while linksN:
  objectN = bucket.get(keyN)
  print(objectN)
  linksN = objectN.links
  print(linksN)
  keyN = linksN[0][KEY]
  print(keyN)


