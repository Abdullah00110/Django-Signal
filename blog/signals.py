from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
# Logic starts here


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("Logged-in Signal --------------->")
    print("Sender --------->", sender)
    print("Request --------->", request)
    print("User --------->", user)
    print("User password ------->", user.password)
    print(f"kwargs ------>{kwargs}")


@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print("Logout successful ------->")
    print("Sender -------->", sender)
    print("Request -------->", request)
    print("User", user)
    print(f"Kwargs -----> {kwargs}")


@receiver(user_login_failed, sender=User)
def login_failed(sender, request, user, **kwargs):
    print("Login failed ------------>")
    print("Sender ------------>", sender)
    print("Request ------------>", request)
    print("User --------->", user)
    print(f"Kwargs {kwargs}")

# user_logged_in.connect(login_success, sender=User)
