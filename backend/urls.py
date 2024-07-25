from django.urls import path
from .views import *

urlpatterns=[
    path('',aboutpage,name='about'),
    path('query/',querypage,name='query'),
    path('login',loginpage,name='login'),
    path('logout',logoutpage,name='logouts'),
    path('signup/',signuppage,name='signup'),
    path('scheme/',schemepage,name='scheme'),
    path('collections',collectionspage,name='collection'),
    path('collection/<str:name>',collectionview,name='collect'),
    path('collect/<str:cname>/<str:pname>',productdetails,name='prodetails'),

]