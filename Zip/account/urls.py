from django.urls import path
from .views import register_request, login_request, logout_view,activity_log,delete_acticity_log,excelreport
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_view, name="logout"),
    path("activity_log", activity_log, name="activity_log"),
    path("delete/log/<int:pk>", delete_acticity_log, name="delete_log"),
    path("excelreport", excelreport, name="excelreport"),


]