# README for riak.referid.co.git

## Overview
Repository for setting up a Riak node using the Erlang OTP.

## Riak
Get Riak:

  sudo apt-get install erlang
  git clone http://github.com/basho/riak
  cd riak
  make rel

## Python
Get the following base Python libraries:
  
  sudo apt-get install python-setuptools

Get the Riak Python Client library:

  sudo apt-get install python-protobuf
  git clone http://github.com/bash/riak-python-client
  cd riak-python-client
  sudo python setup.py install

