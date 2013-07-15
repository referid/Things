% Librarian Daemon
%% Message processing daemon that handles all incoming requests to the key-value store.
-module(librarian).
-export([all]).

Node = 'riak@127.0.0.1'
{ok, Client} = riak:client_connect(Node)

loop() ->
    receive
    {is_registered, Bucket, Key} ->
        read_object:is_registered(...)
        loop();
    {register_object, Bucket, Key, User} ->
        write_object:register_private_object(...)
        loop();
    Nil -> 
        loop()
    end.

    
