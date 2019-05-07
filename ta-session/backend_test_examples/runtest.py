import debttest
import requests
from time import sleep
from random import randint

def find_id(users_json, uname):
    for user_json in users_json:
        if user_json["username"] == uname:
            return user_json["id"]
    print('Cannot find user {0}! Did you run "python manage.py shell < inittest.py"?'.format(uname))
    exit(1)

def find_userinfo(users, q_uid):
    for (uname, upwd, uid) in users:
        if uid == q_uid:
            return (uname, upwd)
    print("Cannot find user with id {0}!".format(q_uid))
    exit(1)

def get_json_or_error(link, uname, upwd):
    sleep(0.05)
    try:
        res = requests.get(link, auth=(uname, upwd))
        if res.status_code != 200:
            print("ERROR: Cannot get {0} : {1}, id = {2}, pwd = {3}".format(link, res.status_code, uname, upwd))
            exit(1)
        resjson = res.json()
        return resjson
    except Exception:
        print("ERROR: Cannot get {0}".format(link))
        exit(1)

def delete_or_error(link, uname, upwd):
    sleep(0.05)
    try:
        res = requests.delete(link, auth=(uname, upwd))
        if res.status_code != 204:
            print("ERROR: Cannot delete {0} : {1}, id = {2}, pwd = {3}".format(link, res.status_code, uname, upwd))
            exit(1)
    except Exception:
        print("ERROR: Cannot delete {0}".format(link))
        exit(1)

def post_or_error(link, data, uname, upwd):
    sleep(0.05)
    try:
        res = requests.post(link, data=data, auth=(uname, upwd))
        if res.status_code != 201:
            print("ERROR: Cannot post {0} : {1}, id = {2}, pwd = {3}".format(link, res.status_code, uname, upwd))
            exit(1)
    except Exception:
        print("ERROR: Cannot post {0}".format(link))
        exit(1)


def forbidden_or_error(method, link, uname, upwd):
    sleep(0.05)
    try:
        if method == "GET":
            res = requests.get(link, auth=(uname, upwd))
        elif method == "DELETE":
            res = requests.delete(link, auth=(uname, upwd))
        elif method == "POST":
            res = requests.post(link, auth=(uname, upwd))
        elif method == "PUT":
            res = requests.put(link, auth=(uname, upwd))
        if res.status_code != 403:
            print("ERROR: Should not be allowed to {0} {1} : code {2}, id = {3}, pwd = {4}".format(method, link, res.status_code, uname, upwd))
            exit(1)
    except Exception:
        print("ERROR: Cannot {0} {1}".format(method, link))
        exit(1)

def forbidden_or_error_anon(method, link):
    sleep(0.05)
    try:
        if method == "GET":
            res = requests.get(link)
        elif method == "DELETE":
            res = requests.delete(link)
        elif method == "POST":
            res = requests.post(link)
        elif method == "PUT":
            res = requests.put(link)
        if res.status_code != 403:
            print("ERROR: Should not be allowed to {0} {1} with no auth : code {2}".format(method, link, res.status_code))
            exit(1)
    except Exception:
        print("ERROR: Cannot get {0}".format(link))
        exit(1)


def check_key(debt_json, key):
    if key not in debt_json:
        print("{0} not in {1}.".format((key, debt_json)))
        exit(1)


userN = 10
user_pairs = debttest.create_users(userN)
admname = "debt_admin"
admpwd = "debt_adminpasswd"
admpwd_wrong = "debt_adminpasswd_wrong"
unknname = "unknown_user"
unknpwd = "unknown_userpwd"

# 1. get id of each user
link = "http://localhost:8000/users/"
print("1. Getting users list.")
forbidden_or_error_anon("GET", link) # anonymous
forbidden_or_error("GET", link, unknname, unknpwd) # unknown user
for (uname, upwd) in user_pairs:
    forbidden_or_error("GET", link, uname, upwd) # users can't see this page
# only admin can get this data
forbidden_or_error("GET", link, admname, admpwd_wrong)
users_json = get_json_or_error(link, admname, admpwd)

users = [ (uname, upwd, find_id(users_json, uname)) for (uname, upwd) in user_pairs ]

# 2. get existing debts
link = "http://localhost:8000/debts/"
print("2. Checking GET {0}".format(link))
forbidden_or_error_anon("GET", link) # anonymous
forbidden_or_error("GET", link, unknname, unknpwd) # unknown user
for (uname, upwd) in user_pairs:
    forbidden_or_error("GET", link, uname, upwd) # users can't see this page
# only admin can get this data
forbidden_or_error("GET", link, admname, admpwd_wrong)
debts_old = get_json_or_error(link, admname, admpwd)

# 3. remove existing debts
link = "http://localhost:8000/debts/"
print("3. Checking DELETE {0}id".format(link))
deletedByAdmin = True
for debt in debts_old:
    link2 = link + str(debt["id"])
    print("\tDeleting debt {0}".format(link))
    forbidden_or_error_anon("DELETE", link2) # anonymous

    lendername = None
    lenderpwd = None
    for (uname, upwd, uid) in users:
        # only lender can erase this
        if debt["lender"] == uid:
            lendername = uname
            lenderpwd = upwd
            continue
        forbidden_or_error("DELETE", link2, uname, upwd)
    forbidden_or_error("DELETE", link2, admname, admpwd_wrong)
    
    if deletedByAdmin:
        delete_or_error(link2, admname, admpwd)
    else:
        delete_or_error(link2, lendername, lenderpwd)
    deletedByAdmin = not deletedByAdmin

# 4. create debts
link = "http://localhost:8000/debts/"
debts = []
debtN = 40
print("4. Checking POST {0} by creating {1} debts.".format(link, debtN))
for i in range(0, debtN):
    amnt = randint(1, 1000)
    borrower = users[randint(0, len(users) - 1)][2]
    while True:
        lender = users[randint(0, len(users) - 1)][2]
        if lender != borrower:
            break
    payload_forstore = {'amount':amnt, 'borrower':borrower, 'lender':lender}
    debts.append(payload_forstore)
    
    payload = {'amount':amnt, 'lender':lender}
    (bname, bpwd) = find_userinfo(users, borrower)
    print("\tposting with user: {0}".format((bname, bpwd)))
    post_or_error(link, payload, bname, bpwd)

print("\tChecking debts created.. : ")

debts_json = get_json_or_error("http://localhost:8000/debts/", admname, admpwd)
if len(debts_json) != len(debts):
    print("ERROR: GET http://localhost:8000/debts/ has more or less items than debts")
    exit(1)

for debt in debts:
    found = False
    for debt_json in debts_json:
        check_key(debt_json, "borrower")
        check_key(debt_json, "lender")
        check_key(debt_json, "id")
        check_key(debt_json, "created")
        check_key(debt_json, "amount")
        if debt_json["borrower"] == debt["borrower"] and debt_json["lender"] == debt["lender"] and debt_json["amount"] == debt["amount"]:
            found = True
            debt["id"] = debt_json["id"]
            debt["created"] = debt_json["created"]
            break
    if not found:
        print("ERROR: Not found : {0}".format(debt))
        exit(1)

print("TEST SUCCESSFUL (further tests will be added)")
