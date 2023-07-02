# importing python module
import json

# importing python components
from django.contrib.auth import login, logout, get_user_model
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# importing our project components
from .serializers import RegisterSerializer


@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == 'GET':
        return Response({
            "status": request.user.is_authenticated
        })
    json_body = json.loads(request.body)
    print(json_body)
    username = json_body.get("username")
    password = json_body.get("password")
    if username and password:
        user_obj = get_user_model().objects.get(username=username)
        if user_obj:
            login(request=request, user=user_obj)
    return redirect("accounts:login")


@api_view(['GET', 'POST'])
def logout_view(request):
    if request.method == 'GET':
        return Response({
            "status": request.user.is_authenticated
        })
    logout(request=request)
    return redirect("accounts:logout")    


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
