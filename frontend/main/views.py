from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.



def index_page(request):
    print "We are in the index_page request..."
    context = ''
    return render(request, '../templates/index.html', context)

