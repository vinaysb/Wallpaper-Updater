#!/usr/bin/env python
import praw
import random
import socket
import sys
import webbrowser


def receive_connection():
    """Wait for and then return a connected socket..

    Opens a TCP connection on port 8080, and waits for a single client.

    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 8080))
    server.listen(1)
    client = server.accept()[0]
    server.close()
    return client


def send_message(client, premessage):
    """Send message to client and close the connection."""
    # print(message)
    if premessage == 0:
        message = 'Successfully connected to reddit'
    else:
        message = premessage
    client.send('HTTP/1.1 200 OK\r\n\r\n{}'.format(message).encode('utf-8'))
    client.close()


def main():
    reddit = praw.Reddit(client_id='szAEvLMd-fUyIQ',
                         client_secret='RUbLmQVrDRVQ3UvxWtRHAFgPyGg',
                         redirect_uri='http://localhost:8080',
                         user_agent='testing refresh toke /u/ByakuyaV')
    state = str(random.randint(0, 65000))
    url = reddit.auth.url(['*'], state, 'permanent')
    webbrowser.open(url)
    sys.stdout.flush()

    client = receive_connection()
    data = client.recv(1024).decode('utf-8')
    param_tokens = data.split(' ', 2)[1].split('?', 1)[1].split('&')
    params = {key: value for (key, value) in [token.split('=')
                                              for token in param_tokens]}

    if state != params['state']:
        send_message(client, 'State mismatch. Expected: {} Received: {}'
                     .format(state, params['state']))
        return 1
    elif 'error' in params:
        send_message(client, params['error'])
        return 1

    refresh_token = reddit.auth.authorize(params['code'])
    send_message(client, 0)
    return refresh_token


def RefreshToken():
    return main()
