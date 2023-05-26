from django.shortcuts import render

def pay(request):
    return  render(request, "pay_view.html")
