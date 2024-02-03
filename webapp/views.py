from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import *
from datetime import datetime


# Create your views here.


def home(request):
    
    news = News.objects.all()
    
    context = {
        'news' : news
    }
    
    return render(request, "pages/home.html", context)


def gallery(request):
    return render(request, "pages/gallery.html")


def sign_in(request):
    if request.user.is_authenticated:
        return redirect(to="dashboard")

    # if request.method == "POST":
    #     user = {
    #         "username": request.POST.get("username"),
    #         "password": request.POST.get("password"),
    #     }
    #     print(user)
    #     userAuth = authenticate(
    #         request, username=user["username"], password=user["password"]
    #     )
    #     print(userAuth)

    # if userAuth is not None:
    #     login(request, userAuth)
    #     return redirect(to="dashboard")
    return render(request, "pages/login.html")


def sign_in_user(request):
    if request.method == "POST":
        user = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
        }
        userAuth = authenticate(
            request, username=user["username"], password=user["password"]
        )
        print(userAuth)
        if userAuth is not None:
            login(request, userAuth)
            return redirect(to="dashboard")

    return render(request, "pages/login.html")


def reservation(request):
    if request.method == "POST":
        reservationData = {
            "name": request.POST.get("name"),
            "date": request.POST.get("reservation_date"),
            "total_person": request.POST.get("total_person"),
            "total_cottage": request.POST.get("total_cottage"),
            "email": request.POST.get("email"),
            "message": request.POST.get("message"),
        }
        Schedule.objects.create(
            name=reservationData["name"],
            date=reservationData["date"],
            total_person=reservationData["total_person"],
            total_cottage=reservationData["total_cottage"],
            email=reservationData["email"],
            message=reservationData["message"],
        )
        return redirect(to="home")
    return redirect(to="home")


@login_required(login_url="login")
def sign_out(request):
    logout(request)
    return redirect(to="home")


@login_required(login_url="login")
def dashboard(request):
    reservations = Schedule.objects.all()
    total_reservations = Schedule.objects.count()
    total_news = News.objects.count()

    context = {
        "reservations": reservations,
        "total_reservations": total_reservations,
        "total_news": total_news,
    }

    return render(request, "pages/dashboard/index.html", context)


@login_required(login_url="login")
def reservation_index(request):
    reservations = Schedule.objects.all()
    total_reservations = Schedule.objects.count()
    context = {
        "reservations": reservations,
        "total_reservations": total_reservations,
    }

    return render(request, "pages/dashboard/reservation/index.html", context)
@login_required(login_url="login")
def reservation_show(request,  reservationID):
    reservation = Schedule.objects.filter(id=reservationID).first()
    context = {
        "reservation": reservation,
    }

    return render(request, "pages/dashboard/reservation/show.html", context)

@login_required(login_url="login")
def reservation_delete(request,  reservationID):
    reservation = Schedule.objects.filter(id=reservationID).first()
    reservation.delete()

    return redirect(to="reservation_index")

@login_required(login_url="login")
def reservation_edit(request,  reservationID):
    reservation = Schedule.objects.filter(id=reservationID).first()
    if request.method == "POST":
         reservationData = {
            "name": request.POST.get("name"),
            "date": request.POST.get("reservation_date"),
            "total_person": request.POST.get("total_person"),
            "total_cottage": request.POST.get("total_cottage"),
            "email": request.POST.get("email"),
            "message": request.POST.get("message"),
        }
         reservation.name=reservationData['name']
         reservation.date=reservationData['date']
         reservation.total_person=reservationData['total_person']
         reservation.total_cottage=reservationData['total_cottage']
         reservation.email=reservationData['email']
         reservation.message=reservationData['message']
         reservation.save()
         
         return redirect(to="reservation_index")
    return render(request, "pages/dashboard/reservation/edit.html", {'reservation' : reservation})

@login_required(login_url="login")
def new_index(request):
    newsList = News.objects.all()
    context = {
        'news' : newsList
    }
    
    return render(request, 'pages/dashboard/news/index.html', context)


@login_required(login_url="login")
def new_create(request):
    
    if request.method == 'POST':
        
        newData = {
            'title' : request.POST.get('title'),
            'content' : request.POST.get('content')
        }
        
        News.objects.create(
            title=newData['title'],
            content=newData['content']
        )
        
        
        
        return redirect(to="new_index")
    
    return render(request,'pages/dashboard/news/create.html')


@login_required(login_url="login")
def new_show(request, newsID):
    
    newData = News.objects.filter(id=newsID).first()
    
    
    return render(request, 'pages/dashboard/news/show.html', {'news' : newData})

@login_required(login_url="login")
def new_delete(request, newsID):
    
    newData = News.objects.filter(id=newsID).first()
    
    newData.delete()
    return redirect(to="new_index")
    
    # return render(request, 'pages/dashboard/news/index.html', context)

# def sign_up(request):

#     return render(request, 'pages/register.html')
