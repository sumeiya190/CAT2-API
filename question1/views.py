# question1/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the question1 app!")
