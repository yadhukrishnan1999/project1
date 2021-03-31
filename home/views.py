from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import render
from home.models import Course

# Create your views here.


def home(request):
    # obj = Course.objects.get(id=1)
    obj = Course.objects.all()
    return render(request, 'college.html', {'ob': obj})


def delete(request, pk):
    ob = Course.objects.get(id=pk)
    ob.delete()
    return redirect('/')


def edit(request, pk):
    if request.method == 'GET':
        obj = Course.objects.get(id=pk)
        return render(request, 'edit.html', {'ob': obj})
    else:
        h = request.POST['h']
        d = request.POST['d']
    Course.objects.filter(id=pk).update(h=h, d=d)
    return redirect('home:home')


def login(request):
    return HttpResponse("Login")
