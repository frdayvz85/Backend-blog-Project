from django.http import HttpResponse
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile, ContactForm, Contact
import sweetify











@login_required

def dashboard(request):

    return render(request,

                  'account/dashboard.html',

                  {'section': 'dashboard'})





def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():

            # Create a new user object but avoid saving it yet

            new_user = user_form.save(commit=False)

            # Set the chosen password

            new_user.set_password(

                user_form.cleaned_data['password'])

            # Save the User object

            new_user.save()

            # Create the user profile

            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})





@login_required

def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')

        else:

            messages.error(request, 'Error updating your profile')

    else:

        user_form = UserEditForm(instance=request.user)

        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request,

                  'account/edit.html',

                  {'user_form': user_form,

                   'profile_form': profile_form})

def logout_view(request):
    logout(request)
    #sweetify.info(request, 'Bele tez gedirsiniz??', button='Ok', timer=3000)
    return redirect('/')


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contactdata = Contact()
            contactdata.name =form.cleaned_data['name']
            contactdata.email =form.cleaned_data['email']
            contactdata.subject =form.cleaned_data['subject']
            contactdata.message =form.cleaned_data['message']
            contactdata.save()

            messages.success(request,"Your message has been sent.Thank you for your interest")

            return HttpResponseRedirect('/account/contact')
    else:
        form = ContactForm()
    return render(request, 'contact1.html', {'form':form})
    