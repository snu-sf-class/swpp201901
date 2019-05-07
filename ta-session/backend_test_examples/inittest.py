from django.contrib.auth.models import User
import debttest
import json
import requests

# First of all, it initializes debt information.
def remove_user(username):
    try:
        user = User.objects.get(username = username)
        user.delete()
        print("\tDeleted user {0}".format(username))
    except User.DoesNotExist:
        # no problem.
        pass
    return

remove_user("debt_admin")
for i in range(1,10):
    username = "test{0}".format(i)
    remove_user(username)

print("---------------")
newusers = [("debt_admin", "debt_adminpasswd")]
newusers = newusers + debttest.create_users(10)
for (username, pwd) in newusers:
    user = User.objects.create_user(username, password=pwd)
    user.save()
    print("\tCreated user {0}".format(username))

print("Initialization Successful!")
