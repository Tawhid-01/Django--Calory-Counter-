from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum

# Create your views here.
@login_required
def DashboardPage(req):



    take_bmr = req.user.profile.bmr

  
    consume_calory = FoodItemModel.objects.filter(user=req.user).aggregate(
        total_calory=Sum('calory')
    )['total_calory'] or 0

    need_calory = take_bmr - consume_calory


    data = UpdatedProfileModel.objects.filter(user=req.user) 

    context = {
        'data': data,
        'take_bmr': round(take_bmr, 2),
        'consume_calory': round(consume_calory, 2),
        'need_calory': round(need_calory, 2)
    }
  
    return render(req, 'pages/dashboard.html', context)


def registerPage(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm-password')

        user_exist =UserModel.objects.filter(username=username).exists()
        email_exist =UserModel.objects.filter(email=email).exists()

        if user_exist and email_exist:
            messages.error(req, 'User already exist')
            return redirect('register')
        else:
            if password == confirm_password:
                UserModel.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                messages.success(req, 'User created successfully')
                return redirect('login')
            else:
                 messages.error(req, 'Password does not match')
                 return redirect('register')


    return render(req, 'account/register.html')

       
def loginPage(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            return redirect('update_profile')
        else:
            messages.error(req, 'Invalid username or password')
            return redirect('login')
    return render(req, 'account/login.html')
        
               
          
def logoutPage(req):
    logout(req)
    return redirect('login')

@login_required
def updateProfilePage(req):
    try:
        user = req.user.profile
    except UpdatedProfileModel.DoesNotExist:
        user = UpdatedProfileModel.objects.create(user=req.user)
    if req.method == 'POST':
        form = UpdatedProfileForm(req.POST, req.FILES, instance=user)
        if form.is_valid():
            data =form.save(commit=False)
            if data.gender == 'M':
                data.bmr =66.47 + (13.75 * data.weight) + (5.003 * data.height) - (6.755 * data.age)
            else:
                data.bmr = 655.1 + (9.563 * data.weight) + (1.850 * data.height) - (4.676 * data.age)
            data.save()

           
            return redirect('dashboard')
    else:
        form = UpdatedProfileForm(instance=req.user.profile)
    context = {
        'form': form,
        'title': 'Update Profile',
        'btn_title': 'Update'
    }
    return render(req, 'base/base_form.html', context)

@login_required
def consumeCaloryPage(req):
    if req.method == 'POST':
        form = FoodItemForm(req.POST)
        if form.is_valid():
            data =form.save(commit=False)
            data.user = req.user
            data.save()
            return redirect('dashboard')
    else:
        form = FoodItemForm()
    context = {
        'form': form,
        'title': 'Consume Calory',
        'btn_title': 'Consume'
    }
        
    return render(req, 'base/base_form.html', context)