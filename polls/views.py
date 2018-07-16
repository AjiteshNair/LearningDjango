from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")     # displays this when address/polls is opened

# Create your views here.
