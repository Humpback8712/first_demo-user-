from django.shortcuts import render
from django.http import HttpResponse
import re
from user.models import User
from django.shortcuts import reverse, redirect


def register(request):
    '''显示注册页面'''
    return render(request, 'register.html')


def register_handle(request):
    '''注册处理'''
    # 接收数据
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')

    # 数据校验
    if not all([username, password, email]):
        return render(request, 'register.html', {'errmsg': '数据不完整'})
    # 校验邮箱
    if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
    # 是否同意协议
    if allow != 'on':
        return render(request, 'register.html', {'errmsg': '请同意协议'})

    # 进行业务处理：进行用户注册
    user = User.objects.create_user(
        username,
        email,
        password
    )
    # 返回应答，返回首页

    return redirect(reverse('user:index'))


def index(request):
    return render(request, 'index.html')
