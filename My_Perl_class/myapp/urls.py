from django.urls import path
from. import views

urlpatterns=[

    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='my_services'),
    path('blog',views.blog,name='my_blog'),


]
