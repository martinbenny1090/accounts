from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.generic.list import View
# Create your views here.
 
def register(request):
    if request.method == 'POST':
        F_name = request.POST['fname']
        L_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        password1 = request.POST['cpass']

        if password==password1:
            if User.objects.filter(username=email).exists():
                print('username taken')
                messages.info(request,'E-mail Id already using')
                return redirect('register')
            else:    
                user = User.objects.create_user(username=email, password=password, email=email,first_name=F_name, last_name=L_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            print('password not matching')
            messages.info(request,'Password not matchng')
            return redirect('register')

    else:
        return render(request, 'user_signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email,password=password)

        if user is not None:
            auth.login(request, user)
            if User.objects.filter(username=email, is_superuser="True").exists():
                messages.info(request,'Admin page')
                return render(request, 'owner/owhome.html')
            else:
                # auth.login(request, user)
                return redirect("/")

        else:
            messages.info(request,'Invalied Login')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def index(request):
    return render(request, 'index.html')

def explore(request):
    return render(request, 'explore.html')

def home(request):
    return render(request, 'userHome.html')

def hotel(request):
    return render(request, 'hotel_login.html')

def hotel_signup(request):
    return render(request, 'hotelSignup.html')

def HotelAdmin(request):
    return render(request, 'hotel_Admin.html')


class hotel_list(View):
    def get(self, request):
        return render(request, 'hotel_list.html')


class city(View):
    def get(self, request):
        return render(request, 'City.html')


class booking(View):
    def get(self, request):
        return render(request, 'booking.html')    

def room_mag(request):
    return render(request, 'room_mag.html')

class room_details(View):
    def get(self, request):
        return render(request, 'hotel/room-details.html')  

def data(request):
    return render(request, 'data.html')





