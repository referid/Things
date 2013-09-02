# ReferID Things

## Overview
Repository for setting up a Riak node using the Erlang OTP.

## Installing Riak
Get Riak:

    sudo apt-get install erlang
    git clone http://github.com/basho/riak
    cd riak
    make rel

## Installing Python
Get the following base Python libraries:
  
    sudo apt-get install python-setuptools

Get the Riak Python Client library:

    sudo apt-get install python-protobuf
    git clone http://github.com/bash/riak-python-client
    cd riak-python-client
    sudo python setup.py install

## Curl Basics in Riak
Adding to the cluster:

    curl -X PUT HTTP://127.0.0.1:8091/riak/bucket/key

    curl -v -d 'CONTENT' -H "Content-Type: text/plain" http://127.0.0.1:8091/riak/bucket

    curl -v -X PUT -d '{"bar":"baz"}' -H "Content-Type: application/json"
    -H "X-Riak-Vclock: a85hYGBgzGDKBVIszMk55zKYEhnzWBlKIniO8mUBAA=="
    http://127.0.0.1:8091/riak/bucket/key?returnbody=true

Mapreduce query for some JSON_SCRIPT:

    curl -X POST http://127.0.0.1:8091/mapred -H "Content-Type: application/json" -d @- JSON_SCRIPT

Attaching a link:
  
    curl -v -X PUT -H 'Link: </riak/BUCKET/KEY>; riaktag="tag"' \
    -H "content-type: text/plain" http://127.0.0.1:8091/riak/bucket/key \
    -d 'CONTENT'

Link walking:
  
    curl -v http://127.0.0.1:8091/riak/bucket/key/bucket,tag,keep

Add a song:

    curl -X PUT HTTP://24.37.29.62:8098/riak/bucket/key  -H "Content-type: audio/mpeg" --data-binary @filename.mp3

