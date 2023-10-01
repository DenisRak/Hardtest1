from django.urls import path

from Register.views import register, user_login, user_logout

urlpatterns = [
    path('register', register, name='Register'),
    path('login', user_login, name='Login'),
    path('logout/', user_logout, name='Logout'),
]