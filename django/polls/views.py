from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        message=request.POST['message']
        email=request.POST['email']
        name=request.POST['name']
        send_mail(
            name,#title
            message,#message
            'settings.EMAIL_HOST_USER', #sender if not available  consider default or configured
            [email]  #receiver can be hardcoded
            )
    return render(request,'hello.html')

# send_mail(
#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["shayan.ms181@gmail.com"],
#     fail_silently=False,
# )


