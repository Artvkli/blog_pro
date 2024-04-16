
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User 
def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('/')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(password = password , username = username )
    if user is not None :
        login(request , user)
        return redirect('home:home')
        print(user)
    return render(request , 'accounts/login.html' )


def user_signup(request):  
    context = {'errors':[] }
    if request.user.is_authenticated == True:
        return redirect('home:home')
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            
            context['errors'].append("pass not same")
            
            return render(request, 'accounts/signup.html', context)
        
        
        user = User.objects.create(username=username, password=password1, email=email)
        login(request ,user)
        return redirect('home:home')
    return render(request, 'accounts/signup.html')
                    
                    
def user_logout(request):
    logout(request)
    return redirect('home:home')
