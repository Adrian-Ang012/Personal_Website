from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'My_WebsiteApp/2.Home_Page.html')