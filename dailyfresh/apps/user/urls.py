from django.urls import path
from user.views import RegisterView, index

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('register/', views.register.as_view(), name='register'),
    path('index/', index, name='index')
]
