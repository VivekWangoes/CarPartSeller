from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from users.models import User
from .forms import RegisterUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import(urlsafe_base64_decode)
from django.utils.encoding import force_str 
from base.messages import Message
from base.utils import send_email_confirmation


class Registration(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterUser(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.password = make_password(request.POST['password'])
            form_obj.save()
            send_email_confirmation(form_obj=form_obj)
            messages.add_message(request, messages.SUCCESS,
                                 Message.REGISTERATION_MESSAGE)
            return redirect('login')
        else:
            user = User.objects.filter(email=request.POST['email']).first()
            if not user.is_active:
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.phone_no = request.POST['phone_no']
                user.save()
                send_email_confirmation(user)
                messages.add_message(request, messages.SUCCESS,
                                    Message.REGISTERATION_MESSAGE)
                return redirect('login')
            messages.add_message(request, messages.WARNING,
                                 Message.ACCOUNT_EXIST)
            return render(request,'register.html', {"form": form})


def login_page(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('parts')
        else:
            messages.add_message(request, messages.WARNING,
                                 Message.CREADENTIAL_INCORRECT)
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def logout_page(request):
    logout(request)
    return redirect('login')



class EmailConfirmation(View):

    def get(self, request, uidb64, token):
        decode_id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.filter(
                            id=decode_id).first()
        if (user and PasswordResetTokenGenerator()
                    .check_token(user, token)):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 Message.ACCOUNT_VERIFICATION_SUCCEEFULL)
            return redirect('login')
        return HttpResponse("Your link has been expired.")