from django.shortcuts import render, render_to_response
from django.http import HttpResponse


def home(request):
    context = {}
    return render_to_response('morado/index.html')

#  def tasklist(request):
 #   context = {}
 #   return render_to_response('morado/tasklist.html')
