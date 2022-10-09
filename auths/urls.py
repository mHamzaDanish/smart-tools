from django.urls import path
from auths.views import *

urlpatterns = [


#========== Authentication ================#
    path('login/',  login,     name = 'login'),
    path('logout/', logout_,   name = 'logout'),
    path('signup/', register,  name = 'signup'),
#========== Authentication ================#


]
