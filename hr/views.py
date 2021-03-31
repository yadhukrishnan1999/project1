from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import render
from .forms import studentForm
from .models import Student1
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def register(request):
    if request.method == 'GET':
        form = studentForm()
        return render(request, 'about.html', {'form': form})
    else:
        form = studentForm(request.POST)
        form.save()
        form = studentForm()
        return render(request, 'about.html', {'form': form})


def studRegister(request):
    if request.method == 'POST':
        name = request.POST['user']
        age = request.POST['age']
        Student1.objects.create(name=name, age=age)
        return render(request, 'about.html')
    else:
        return render(request, 'about.html')


def hr_about(request):
    return render(request, 'about.html')


def hr_login(request):
    return HttpResponse("hr login")

def send_email(request):
    subject = 'welcome to GFG world'
    message = "hello welcome "
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.GET['email'],]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('home:home')


def test():
    pass