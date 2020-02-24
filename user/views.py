from django.shortcuts import render, redirect
from rest_framework import generics
from django.contrib.auth.decorators import login_required

from . import models
from . import serializers

# Create your views here.

@login_required()
def handle_login(request):
    """
    Handle user login
    """
    context = {}
    return render(request, 'user/home.html', context)


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
