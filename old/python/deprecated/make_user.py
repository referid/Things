# write_private_user.py/3
# bind client and bind inputs
import riak
import hashlib

def make_user(user_name, user_email, user_password):
    client = riak.RiakClient()
    user_name_hash = hashlib.sha224(user_name).hexdigest()
    users_bucket = client.bucket(user_name_hash)
    user_data = {'user_name': user_name,'user_email': user_email,'user_password': user_password,'is_public': 'false'}
    new_user = users_bucket.new('main', user_data)				 
    new_user.store()
