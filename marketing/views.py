from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model, logout
#import sweetify

# Create your views here.



def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request, user)
       # sweetify.info(request, 'Sweet!', text='Here is a custom image', imageUrl='/static/images/profıl2.jpg', timer=5000)
        #sweetify.success(request, 'Başarılı bir şekilde giriş yaptınız', button='Ok')
        return redirect('post-list')
    return render(request, 'accounts/form.html', {'form':form, 'title':'Sign In'})


#User = get_user_model()
def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
       # user = form.cleaned_data.get("username")
       # email = form.cleaned_data.get("email")
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        #user.is_staff = user.is_superuser = True 
       # user.is_superuser = True
        #new_user = User.objects.create_user(username, email, password)
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('post-list')
        #print(new_user)
    return render(request, 'accounts/form.html', {'form':form, 'title':'Register'})



def logout_view(request):
    logout(request)
    #sweetify.info(request, 'Bele tez gedirsiniz??', button='Ok', timer=3000)
    return redirect('post-list')







