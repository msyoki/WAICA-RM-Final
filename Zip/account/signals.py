from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from account.models import UserActivityLog
import socket
from urllib.parse import urlparse

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    if not user.is_superuser:
        hostname = socket.gethostbyname(urlparse(request.META.get('HTTP_REFERER')).hostname)
        IPAddr = socket.gethostbyname(hostname)   
        full_name= f"{user.first_name} {user.last_name}"
        UserActivityLog.objects.create(user_email=user.email,ip_address=IPAddr,activity="login",country=user.country,user_name=full_name)
	# print(f"user {user.first_name} {user.last_name} logged in through page {request.META.get('HTTP_REFERER')}")
	

@receiver(user_login_failed)
def log_user_login_failed(sender,credentials,request,**kwargs):
    hostname = socket.gethostbyname(urlparse(request.META.get('HTTP_REFERER')).hostname)
    IPAddr = socket.gethostbyname(hostname)   
    UserActivityLog.objects.create(user_email=credentials['username'],ip_address=IPAddr,activity="Failed login")
    print(f"user {credentials['username']} failed to login through page {request.META.get('HTTP_REFERER')}")
    

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    if not user.is_superuser:
        hostname = socket.gethostbyname(urlparse(request.META.get('HTTP_REFERER')).hostname)
        IPAddr = socket.gethostbyname(hostname) 
        full_name= f"{user.first_name} {user.last_name}"
        UserActivityLog.objects.create(user_email=user.email,ip_address=IPAddr,activity="logout",country=user.country,user_name=full_name)
        print(f"user {user.first_name} {user.last_name} logged out through page {request.META.get('HTTP_REFERER')}")


def custom_receiver(user,request,page_activity):
    # if not user.is_superuser:
        hostname = socket.gethostbyname(urlparse(request.META.get('HTTP_REFERER')).hostname)
        IPAddr = socket.gethostbyname(hostname) 
        IPAddr = socket.gethostbyname(hostname)   
        full_name= f"{user.first_name} {user.last_name}"
        UserActivityLog.objects.create(user_email=user.email,ip_address=IPAddr,activity=page_activity,country=user.country,user_name=full_name)