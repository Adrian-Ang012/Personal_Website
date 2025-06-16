from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'My_WebsiteApp/1.base.html')