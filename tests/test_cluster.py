## Test Cluster
##
import riak
import time

client = riak.RiakClient()
bucket = client.bucket('test')
test_object = bucket.new('test', data = {'tested_on': time.time()})
test_object.store()
