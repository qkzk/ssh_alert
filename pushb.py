from pushbullet import Pushbullet
from time import sleep
from pprint import pprint


def readtoken(filename):
    with open(filename) as f:
        return f.readline().strip()


def send_pushbullet(title, body, typ="note"):
    api_key = readtoken("token")
    pb = Pushbullet(api_key)

    if typ == "link":
        sender = pb.push_link
    else:
        sender = pb.push_note

    push = sender(title, body)
    pprint(push)


if __name__ == '__main__':
    send_pushbullet("title", "body")
