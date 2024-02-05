from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User

# Logic starts here


def login_success(sender, request, user, **kwargs):
    print("Logged-in Signal --------------->")
    print("Sender --------->", sender)
    print("Request --------->", request)
    print("User --------->", user)
    print("kwargs ------>", kwargs)


user_logged_in.connect(login_success, sender=User)