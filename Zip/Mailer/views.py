from logging import exception
from django.shortcuts import render, redirect
from PreviewApp.models import Technical, MappedTechnical
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core import settings
import os
from .utilities import sendemail
from account.signals import custom_receiver



# Create your views here.
@login_required(login_url='account:login')
def Mailer(request, foo):
    mailer = True
    technical = Technical.objects.filter(ReceiptNumber__icontains=foo)
    mappedtechnical = MappedTechnical.objects.filter(
        ReceiptNumber__icontains=foo)
    filename = foo + ".pdf"
    filepath = os.path.join(settings.FILES_DIR, filename)
    context = {
        'mailer': mailer,
        'filepath': filepath,
        'receipt_number': foo,
        'sendtechnical': technical,
        'sendmappedtechnical': mappedtechnical,

    }
    return render(request, 'mailer/mailer.html', context)


@login_required(login_url='account:login')
def SendTechnicalMail(request, foo):
    user=request.user
    technical=Technical.objects.filter(ReceiptNumber=foo)
    for i in technical:
        if not i.ReceiverEmail:
            messages.error(request, "Receiver email is missing, please update")
            return redirect('PreviewApp:preview', foo=foo)

        else:
            try:
                response = sendemail(foo)
            except BaseException:
                messages.error(request, "Mail not sent, something went wrong")
            
            if response == 'Done':
                
                # log activity
                page_activity=f"Mailed {i.Category} #{foo}"
                custom_receiver(user,request,page_activity)

                Technical.objects.filter(ReceiptNumber=foo).update(SendStatus=True)
                messages.success(request, "Successfully queued for mailing in 5 min")
                return redirect('PreviewApp:preview', foo=foo)
            
            messages.warning(request, "Recently queued for mailing, try again later")
            
            return redirect('PreviewApp:preview', foo=foo)


@login_required(login_url='account:login')
def SendMappedTechnicalMail(request, foo):
    user=request.user
    mappedtechnical=MappedTechnical.objects.filter(ReceiptNumber=foo)
    for i in mappedtechnical:
        if not i.ReceiverEmail:
            messages.error(request, "Receiver email is missing, please update")
            return redirect('PreviewApp:preview', foo=foo)

        else:
            try:
                response = sendemail(foo)
            except BaseException:
                messages.error(request, "Mail not sent, something went wrong")
            
            if response == 'Done':

                # log activity
                page_activity=f"Mailed {i.Category} #{foo}"
                custom_receiver(user,request,page_activity)

                MappedTechnical.objects.filter(
                    ReceiptNumber=foo).update(
                    SendStatus=True)
                messages.success(request, "Successfully queued for mailing in 5 min")
                return redirect('PreviewApp:preview', foo=foo)
            messages.warning(request, "Recently queued for mailing, try again later")

            return redirect('PreviewApp:preview', foo=foo)