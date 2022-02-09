from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    request.session['view_count'] = request.session.get('view_count', 0) + 1
    if request.session['view_count'] > 5:
        request.session['view_count'] = 1
    resp = HttpResponse('view count={}'.format(request.session['view_count']))
    resp.set_cookie('dj4e_cookie', '5f8d8411', max_age=1000)
    return resp