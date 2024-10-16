from django.http import HttpResponse # type: ignore


def key(request):
    return HttpResponse("hello ,you are at the about ")

# Create your views here.
