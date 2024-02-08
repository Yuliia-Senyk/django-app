from django.urls import path
from playground import views

urlpatterns = [
    path("", views.sayHello),
    path("image", views.sendImage),
    path("html", views.sendHtml),
    path("json", views.sendJSON),


    path("hello/big", views.sayBig),
    path("hello/custom", views.sayBigCustom),
    path("crud/", views.handleCrud),


    path('set_cookie/', views.set_cookie),
    path('get_cookie/', views.get_cookie),
    path('get_headers/', views.get_headers),


    path('users/', views.get_users),

]