from django.contrib import admin
from django.urls import path
from c2c import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('job/', views.job, name='job'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('signup/', views.signup, name='signup'),  
    path('cart/',views.cart,name='cart'),
    path('about',views.about,name='about'),
    path('soft',views.soft,name='soft'),
    path('dm',views.dm,name='dm'),
    path('f_m',views.f_m,name='f_m'),
    path('softdev',views.softdev,name='softdev'),

]