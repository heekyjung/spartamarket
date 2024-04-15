from django.shortcuts import render, redirect


def list(request):
    return render(request, "products/list.html")


def create(request):
    return render(request, "products/create.html")


def detail(request, pk):
    return render(request, "products/list.html")


def update(request, pk):
    return render(request, "products/list.html")


def delete(request, pk):
    return render(request, "products/list.html")


def like(request, pk):
    return render(request, "products/list.html")
