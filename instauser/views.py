from django.shortcuts import render , redirect
from instauser.models import InstaUser

# 221002 최해민 유저생성 검증을 위한 함수 import
from django.contrib.auth import get_user_model # 사용자가 DB안에 있는지 검사하는 함수.
from django.contrib.auth import  authenticate,login ,logout


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user=user)
            return redirect('instauser:profile')
        else:
            return redirect('instauser:login')

def logout_view(request):
    logout(request)
    return redirect('instauser:login')


def profile_view(request):
    return render(request,'profile.html')
    

# 220930 최해민 회원가입후 로그인페이지로 보내기 위한 함수
# def login(request):
#     return render(request, 'login.html')

# 220930 최해민 회원가입 기능 함수
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email') # 이메일 양식이 맞는지 확인..??
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        is_dating = request.POST.get('is_dating')
        
        # 221002 최해민 password가 올바른지 확인하는 분기문
        if password != password2: # password와 password2가 같지 않다면
            return render(request, 'signup.html', {'error' : '비밀번호를 확인해 주십시오.'}) # error를 넘겨주어 알람을 보여준다.
        
        else: # password 확인이 맞을때
            if email == "" or password == "": # 이메일과 패스워드가 공란일 때
                return render(request, 'signup.html', {'error' : '이메일 또는 비밀번호를 입력 안하셨습니다.'})
            
            # 221002 최해민 이미 존재하는 유저가 있는지 확인하기 위한 변수 선언(True, False로 반환)
            exist_user = get_user_model().objects.filter(email = email)
            
            if exist_user: # 이미 존재하는 유저가 있을 때
                return render(request, 'signup.html', {'error' : '동일한 Email이 존재합니다.'})
            
            else:
                instauser = InstaUser(email = email,
                                      name = name,
                                      nickname = nickname,
                                      password = password,
                                      is_dating = is_dating,)
                
                instauser.save()
                
                return redirect('instauser:login')
        
    
    if request.method == 'GET':
        return render(request, 'signup.html')

