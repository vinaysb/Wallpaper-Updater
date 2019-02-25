import praw
import random
import socket
import sys
import webbrowser


def receive_connection():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("localhost", 8080))
    server.listen(1)
    client = server.accept()[0]
    server.close()
    return client


def send_message(client, premessage):
    file = open("templates/redirect.html", "r")
    if premessage == 0:
        message = "Successfully connected to reddit"
    else:
        message = premessage

    http_response = """\
    http/1.1 200 OK
    Content-Type: text/html
    Content-Type: image/png
    Connection: close

    """ + file.read() % message + """
    """
    file.close()
    client.sendall(bytes(http_response, "utf-8"))
    client.close()


def main():
    reddit = praw.Reddit(client_id="szAEvLMd-fUyIQ",
                         client_secret="RUbLmQVrDRVQ3UvxWtRHAFgPyGg",
                         redirect_uri="http://localhost:8080",
                         user_agent="testing refresh token /u/ByakuyaV")
    state = str(random.randint(0, 65000))
    url = reddit.auth.url(["*"], state, "permanent")
    webbrowser.open(url)
    sys.stdout.flush()
    client = receive_connection()
    data = client.recv(1024).decode("utf-8")
    param_tokens = data.split(" ", 2)[1].split("?", 1)[1].split("&")
    params = {key: value for (key, value) in [token.split("=")
                                              for token in param_tokens]}

    if state != params["state"]:
        send_message(client, "State mismatch. Expected: {} Received: {}"
                     .format(state, params["state"]))
        return 1
    elif "error" in params:
        send_message(client, params["error"])
        return 1

    refresh_token = reddit.auth.authorize(params["code"])
    send_message(client, 0)
    return refresh_token


def RefreshToken():
    return main()
