from django.urls import path
from playground import views
from playground import viewsNode

urlpatterns = [
    path("", views.sayHello),
    path("image", views.sendImage),
    path("html", views.sendHtml),

     # endpoint that reads req and sends any json
     path("json", viewsNode.send_random_JSON), 
    
    # these 2 endpoints redirect requests to express app
    # better to have separate django app
    # that redirects all requests with url 'express'
    # to your express app. 
    path("express", viewsNode.redirect_GET_req_to_express),
    path("express/post", viewsNode.redirect_POST_req_to_express),


    path("hello/big", views.sayBig),
    path("hello/custom", views.sayBigCustom),
    path("crud/", views.handleCrud),
    path('set_cookie/', views.set_cookie),
    path('get_cookie/', views.get_cookie),
    path('get_headers/', views.get_headers),
    path('users/', views.get_users),
    path('ws/', views.my_websocket),
    path('db', views.handle_db),
    path('<str:random>/', views.openHelloPage, name='random'),

]