from django.shortcuts import render
from re import template
from django.http import HttpResponse

def index(request):
    return render(request, 'guess/index.html', {})

# Create your views here.
def guess(request, guessvalue):
    context = {
        'guess_value': guessvalue,
        'target_value': 30,
    }
    return render(request, 'guess/result.html', context)