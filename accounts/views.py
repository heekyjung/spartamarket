from django.shortcuts import render, redirect


def login(request):
    return render(request, "accounts/login.html")


def logout(request):
    return render(request, "products/list.html")


def signup(request):
    return render(request, "accounts/signup.html")


def update(request):
    return render(request, "accounts/update.html")


def delete(request):
    return render(request, "products/list.html")
