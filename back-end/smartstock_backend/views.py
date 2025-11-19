from django.http import HttpResponse

def test_view(request):
    return HttpResponse("testing route")

def index_view(request):
    return HttpResponse("<h1>Well come. Home page!</h1>")