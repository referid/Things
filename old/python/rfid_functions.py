## RFID Functions
## by Trevor Stanhope

# Libraries
import riak
import time
import hashlib

# Toolbox
def read_object(object_hash, object_key):
    client = riak.RiakClient()
    object_bucket = client.bucket(object_hash)
    if object_bucket.get(object_key).exists():
        object_binary = object_bucket.get(object_key)
        impression_key = hashlib.sha224(str(time.time)).hexdigest()
        impression_data = {'time': time.time()}
        impression_binary = object_bucket.new(impression_key, impression_data)
        return object_binary
    else:
        pass

def write_object(object_hash, object_key, object_data):
    client = riak.RiakClient()
    object_bucket = client.bucket(object_hash)
    new_object = object_bucket.new(object_key, object_data)
    new_object.store()

def check_object(object_binary): 
    object_data = object_binary.get_data()
    object_type = object_data['type']
    if object_type:
        return (object_type, object_data) # returns (TYPE,DATA) tuple
    else:
        return (None, None) # returns (NONE,NONE) tuple
