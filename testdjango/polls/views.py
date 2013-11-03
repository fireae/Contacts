# Create your views here.
from django.http import HttpResponse, HttpRequest

def index(request):
    return HttpResponse("Hello world")
