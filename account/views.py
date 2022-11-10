from django.shortcuts import render, redirect
from urllib3 import HTTPResponse
from account.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from account.forms import CustomAuthenticationForm
from .verify_recaptcha import verify_rectcha
from account.models import UserActivityLog
from account.filters import UserActivityLogFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def register_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("PreviewApp:home")
        messages.error(
            request,
            "Unsuccessful registration. Invalid information.")
    form = UserCreationForm()
    return render(
        request=request,
        template_name="auth/signup.html",
        context={
            "register_form": form})


def login_request(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                ''' reCAPTCHA validation '''
                result = verify_rectcha(request)

                ''' if reCAPTCHA returns True '''
                if result['success']:
                    if user.is_superuser:
                        login(request, user)
                        # or your url name
                        return redirect('/techedgesupers3cret4dm1n/')
                    else:
                        login(request, user)
                        messages.success(request, "Login Successful.")
                        return redirect('PreviewApp:home')
                ''' if reCAPTCHA returns False '''
                messages.error(
                    request, f"Please check the reCATCHA security box")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = CustomAuthenticationForm()
    return render(
        request=request,
        template_name="auth/login.html",
        context={
            "login_form": form})

def logout_view(request):
    logout(request)
    return redirect("account:login")

@login_required(login_url='account:login')
def activity_log(request):
    user_list = UserActivityLog.objects.all()
    user_filter = UserActivityLogFilter(request.GET, queryset=user_list)
    user_list = user_filter.qs
    
    paginator = Paginator(user_list, 5)
    page = request.GET.get('page', 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    args = {'paginator': paginator,'filter':user_filter, 
        'users':users}
    return render(request, 'activity_log.html', args)


@login_required(login_url='account:login')
def delete_acticity_log(request,pk):
    if request.user.is_superuser:
        UserActivityLog.objects.get(pk=pk).delete()
        messages.success(request, f"log #{pk} successfully deleted.")
        return redirect('account:activity_log')
    messages.error(request, f"Resticted action.")
    return redirect('account:activity_log')



from django.http import HttpResponse
import xlwt
import datetime

@login_required(login_url='account:login')
def excelreport(request):
    response= HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']=f'attachment; filename=RM User Activity Log - {str(datetime.datetime.now())}.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws= wb.add_sheet('User Log')
    row_num= 0
    font_style=xlwt.XFStyle()

    font_style.font.bold=True

    columns = ['Date','Time','Activity','IP Address','Email','Full Name','Country']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    
    font_style=xlwt.XFStyle()

    rows= UserActivityLog.objects.all().values_list(
        'date','time','activity','ip_address','user_email','user_name','country'
    )

    for row in rows:
        row_num +=1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response