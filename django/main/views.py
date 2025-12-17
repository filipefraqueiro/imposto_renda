from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def root(request):
    template_data = {}
    rend = render(request, "root.html", template_data)
    resp = HttpResponse(rend)
    return resp 