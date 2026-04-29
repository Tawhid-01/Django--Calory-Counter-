from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('dashboard/', DashboardPage, name='dashboard'),
    path('consume_calory/', consumeCaloryPage, name='caloruConsume'),
    path('update_profile/', updateProfilePage, name='update_profile'),

]