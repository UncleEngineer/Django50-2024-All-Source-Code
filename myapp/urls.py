from django.urls import path
#from .views import Home, Sawatdee, AboutUs, Contact, Tracking
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('aboutus', AboutUs, name='about-us'), # www.loongshop.com/aboutus
    path('contact', Contact, name='contact'), # www.loongshop.com/contact
    path('tracking', TrackingPage, name='tracking'), 
    path('ask', Ask, name='ask'), 
    path('sawatdee', Sawatdee),
    path('questions', Questions,name='questions'),
    path('answer/<int:askid>', Answer, name='answer'),
]