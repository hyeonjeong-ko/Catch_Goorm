from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                return redirect(next_url if next_url else 'home')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        else:
            return render(request, 'login.html', {'error': 'Please fill in all fields'})

    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        password = request.POST['password']

        # 사용자 생성 및 비밀번호 해시 처리
        user = User.objects.create(
            username=username,
            first_name=first_name,
            password=make_password(password)
        )

        # 회원가입 후 로그인 페이지로 리다이렉트
        return redirect('login')
    return render(request, 'signup.html')

@login_required
def home_view(request):
    return render(request, 'home.html', {'user': request.user})

@login_required
def update_view(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        user.username = request.POST.get('username', user.username)
        user.first_name = request.POST.get('first_name', user.first_name)
        if request.POST.get('password'):
            user.password = make_password(request.POST['password'])
        user.save()

        # 로그아웃시키고 로그인 페이지로 리다이렉트
        logout(request)
        return redirect('login')
    return render(request, 'update.html', {'user': user})

@login_required
def delete_view(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        user.delete()
        logout(request)
        return redirect('login')
    return render(request, 'delete.html', {'user': user})
