from django.urls import path
from bootstrapapp import views

urlpatterns=[
    path('',views.index,name='home'),

    path('about/',views.about,name='About'),

    path('contact/',views.contact,name='Contact Us'),

    path('portfolio/',views.portfolio,name='Portfolio'),

    path('service/',views.services,name='Services'),


]