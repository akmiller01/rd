from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import *

# Create your views here.
def index(request):
    user = request.user
    return render_to_response('core/index.html', {"user":user})