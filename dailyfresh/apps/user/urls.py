from django.urls import path
from user.views import RegisterView, index, Login, LogoutUser

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('register/', views.register.as_view(), name='register'),
    path('index/', index, name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout'),

]
