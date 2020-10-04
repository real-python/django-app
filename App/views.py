from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import *


# def employee(request):
#     e = Emp.objects.all()
#     return render(request, 'App/emp.html', context={'e': e})


# def student(request):
#     s = Stu.objects.all()
#     return render(request, 'App/stu.html', context={'s': s})


def signup_view(request):
    try:
        user_email = request.session['user_email']
        return redirect('/')
    except:
        pass
    if request.method == 'GET':
        return render(request, 'App/signup.html', context={})
    try:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        userimage = request.FILES['userimage']
        username = email.split('@')[0]
        birthday = birthday.split('/')
        birthday = str(birthday[2]) + "-" + str(birthday[1]) + "-" + str(birthday[0])
        print(firstname, lastname, phone, email, username, password, birthday, gender, userimage)
        u = User(
            username=username, first_name=firstname, last_name=lastname, email=email, is_active=True
        )
        u.save()
        u.set_password(password)
        u.save()
        ud = UserDetails(user=u, phone=phone, birthday=birthday, gender=gender, userimage=userimage)
        ud.save()
        return redirect('/login/')

    except Exception as e:
        print(e)
        return redirect('/signup/')


def login_view(request):
    try:
        user_email = request.session['user_email']
        return redirect('/')
    except:
        pass
    if request.method == 'GET':
        return render(request, 'App/login.html', context={})
    try:
        email = request.POST['email']
        password = request.POST['password']

        u = User.objects.get(email=email)
        if check_password(password, u.password):
            request.session['user_email'] = email
            return redirect('/')
        else:
            return redirect('/login/')
    
    except Exception as e:
        print(e)
    return redirect('/login/')


def logout_view(request):
    try:
        del request.session['user_email']
        return redirect('/login/')
    except:
        return redirect('/login/')


def home_view(request):
    try:
        user_email = request.session['user_email']
        ud = UserDetails.objects.get(user__email=user_email)
        blog = Blog.objects.all()
        context = {'ud': ud, 'blog': blog}
        return render(request, 'App/home.html', context=context)
    except:
        return redirect('/login/')


def create_post(req):
    try:
        user_email = req.session['user_email']
        if req.method == 'GET':
            return render(req, 'App/createpost.html', context={})
        else:
            heading = req.POST['heading']
            content = req.POST['content']
            mytag = req.POST['mytag']
            myfile = req.FILES['myfile']

            ud = UserDetails.objects.get(user__email=user_email)
            b = Blog(
                heading=heading, content=content, tag=mytag, image=myfile, user=ud
            )
            b.save()
            return redirect('/')
    except Exception as e:
        print(e)
        return redirect('/login/')
    