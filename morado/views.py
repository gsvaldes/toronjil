from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'morado/index.html'
    



#def home(request):
#    context = {}
#    return render_to_response('morado/index.html')

#  def tasklist(request):
 #   context = {}
 #   return render_to_response('morado/tasklist.html')
