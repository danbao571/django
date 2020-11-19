from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from user.forms import RegisterForm
from user.models import UserProfile
from django.http import JsonResponse
# Create your views here.


@csrf_exempt
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = UserProfile()
            user.username = request.POST.get('username', '')
            user.password = request.POST.get('password', '')
            user.save()
            # del request.session['register_code']
            # 登录用户
            user = auth.authenticate(username=user.username, password=user.password)
            auth.login(request, user)
            return render(request, 'home.html', locals())
        return render(request, 'user/register.html')


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    if request.method == 'POST':
        name = request.POST.get('user')
        password = request.POST.get('password')
        user = auth.authenticate(username=name, password=password)
        data = {}
        if user:
            auth.login(request, user)
            data['username'] = user.username
            data['status'] = "SUCCESS"
        else:
            data['status'] = 'ERROR'
        return JsonResponse(data)


def logout(request):
    auth.logout(request)
    return redirect('/')


def user(request):
    return render(request, 'user/user_info.html', locals())
