import requests
from time import sleep


SUCC=0
FAIL=1
INVALID=2
ERROR=3

def check_status(status):
    if status >= 200 and status < 300:
        return SUCC
    elif status >= 400 and status < 500:
        return FAIL
    else:
        return INVALID


def get(url):
    sleep(0.05)
    try:
        res = requests.get(url)
        return (check_status(res.status_code), res)
    except Exception:
        print("ERROR: cannot get {0}".format(url))
        return (ERROR, False)

def get_auth(url, name, pw):
    sleep(0.05)
    try:
        res = requests.get(url, auth=(name, pw))
        return (check_status(res.status_code), res)
    except Exception:
        print("ERROR: cannot get {0}".format(url))
        return (ERROR, False)

def post_auth(url, name, pw, data):
    sleep(0.05)
    try:
        res = requests.post(url, auth=(name, pw), data=data)
        return check_status(res.status_code)
    except Exception:
        print("ERROR: cannot post {0}".format(url))
        return ERROR

def put_auth(url, name, pw, data):
    sleep(0.05)
    try:
        res = requests.put(url, auth=(name, pw), data=data)
        return check_status(res.status_code)
    except Exception:
        print("ERROR: cannot put {0}".format(url))
        return ERROR

def delete_auth(url, name, pw):
    sleep(0.05)
    try:
        res = requests.delete(url, auth=(name, pw))
        return check_status(res.status_code)
    except Exception:
        print("ERROR: cannot delete {0}".format(url))
        return ERROR

def print_succ(res, score, d):
    if res == SUCC:
        print("O")
        score += d
    elif res == FAIL:
        print("X")
    elif res == INVALID:
        print("I")
    else:
        print("E")
    return score

def print_fail(res, score, d):
    if res == SUCC:
        print("X")
    elif res == FAIL:
        print("O")
        score += d
    elif res == INVALID:
        print("I")
    else:
        print("E")
    return score


url_meetings = "http://127.0.0.1:8000/meetings/"
url_users = "http://127.0.0.1:8000/users/"

since = [
        "2020-01-01T00:00:00.000001Z"
        ]

till = [
        "2020-01-01T02:00:00.000000Z"
        ]

meetings = [
        {'sinceWhen': since[0], 'tilWhen': till[0]}     # 0
        ]

score = 0


print("********************************")
print("1. Create meetings")

res = post_auth(url_meetings, "user0", "password", meetings[0])
score = print_succ(res, score, 1)

print("********************************")

print("Score: " + str(score))
