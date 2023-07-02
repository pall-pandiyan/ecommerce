from django.urls import path
from . import views


urlpatterns = [
    path('register/', view=views.RegisterView.as_view(), name='register'),
    path('login/', view=views.login_view, name='login'),
    path('logout/', view=views.logout_view, name='logout'),
]
