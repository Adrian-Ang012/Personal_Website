from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

def contact_success(request):
    return render(request, "My_WebsiteApp/2.Home_Page.html")

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        body = f"From: {name}\nEmail: {email}\n\n{message}"

        mail = EmailMessage(
            subject="PERSONAL WEBSITE MESSAGE",
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=["chaewonnie62@gmail.com"],
            reply_to=[email],
        )
        mail.send(fail_silently=False)

        return redirect("contact_success")

    return render(request, "contact.html")


def home_page(request):
    return render(request, 'My_WebsiteApp/2.Home_Page.html')