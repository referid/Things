## Register Object
import riak
import hashlib

def register_object(object_hash, object_key, user_hash, user_key):
    client = riak.RiakClient()
    object_bucket = client.bucket(object_hash)
    private_object = object_bucket.get(object_key)
    user_bucket = client.bucket(user_hash)
    private_user = user_bucket.get(user_key)
    
    # make link from object to user
    private_object.add_link(private_user)
    private_object.store()
