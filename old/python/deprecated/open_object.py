## Open Object
import riak
import uuid
import time

def open_object(bucket_hash, object_hash, user_key, user_pass):
    client = riak.RiakClient() # bind pb_client
    private_bucket = client.bucket(bucket_hash)# bind private object's bucket
    if private_bucket.get(object_hash): # as long as it exists, make an impression object
        impression_hash = uuid.uuid1()
        object_data = {'time': time.time(),'private_object': object_hash,'viewed_by': user_key}
        impression = private_bucket.new(impression_hash, object_data)
        private_object = private_bucket.get(object_hash)
        private_object.add_link(impression, 'impression')
        private_object.store()
        impression.store() # store to kv
        private_object_data = private_object.get_data()
        if private_object_data['owned_by'] == user_key:
            pass
        else:
            pass
    else: 
        pass
    

