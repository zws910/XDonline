from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render

from users.models import UserProfile


class CustomBackend(ModelBackend):
    """
    邮箱和用户名都可以登录
    继承基础ModelBackend类, 因为有authenticate方法
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))

            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None







def user_login(request):
    """用户名密码登录"""
    if request.method == "POST":
        # 获取用户提交的用户名和密码
        user_name = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # 成功返回user对象, 失败None
        user = authenticate(username=user_name, password=password)
        # 如果不是null说明验证成功
        if user is not None:
            # 登录
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})

    elif request.method == 'GET':
        return render(request, 'login.html')
