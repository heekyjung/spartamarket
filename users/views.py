from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model


def profile(request, username):
    return render(request, "products/list.html")


def follow(request, username):
    return render(request, "products/list.html")
