from django.shortcuts import render
from DjangoModel.forms import wanafunziform


def home(request):
    stu = wanafunziform
    return render(request, 'index.html', {'form': stu})
