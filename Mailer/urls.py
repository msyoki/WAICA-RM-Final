from django.urls import path
from .views import Mailer, SendMappedTechnicalMail, SendTechnicalMail

app_name = 'Mailer'

urlpatterns = [
    path('preview/<slug:foo>', Mailer, name="mailer"),
    path('mappedtechnical/mail/<slug:foo>', SendMappedTechnicalMail, name="sendmapped"),
    path('technical/mail/<slug:foo>', SendTechnicalMail, name="sendtechnical"),

]
