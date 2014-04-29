from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
def hello(request):
    return HttpResponse('THIS IS http://localhost/hello')

@ensure_csrf_cookie
def home(request):
    return render_to_response('index.html', {'variable': 'world'})
@ensure_csrf_cookie
def edit(request):
    if request.is_ajax():
        message = "Yes, AJAX!"
    else:
        message = "Not Ajax"
    return HttpResponse(message)