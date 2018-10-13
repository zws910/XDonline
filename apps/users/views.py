from django.contrib.auth import authenticate, login
from django.shortcuts import render


# Create your views here.
def user_login(request):
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
