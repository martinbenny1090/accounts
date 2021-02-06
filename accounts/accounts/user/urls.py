from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

from user.views import city,home,booking,room_details,hotel_list

app_name='user'

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    
    
    ###################user ruls views
    path('', views.index, name="index"),
    path('explore', views.explore, name="explore"),
    path('u_home', views.home, name="u_home"),
    path('hotel_login', views.hotel, name="hotel_login"),
    path('hotel_signup', views.hotel_signup, name="hotel_signup"),
    path('hoteladmin', views.HotelAdmin, name="hoteladmin"),


    path('hotel_list', hotel_list.as_view(), name="hotel_list"),
    path('city', city.as_view(), name="city"),
    path('room-details', room_details.as_view(), name="room-details"),
    path('room_management', views.room_mag, name="room_management"),
    path('booking', booking.as_view(), name="booking"),
    path('data', views.data, name="data"),

    

]


'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''