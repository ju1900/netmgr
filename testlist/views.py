from django.shortcuts import render
from testlist.models import *
from django.http import HttpResponse

def testlist(request):
    return render(request, 'testlist/testlist.html')

def product(request, id):
    return render(request, 'testlist/product.html', {'id': id})

def chapter(request, id):
    return render(request, 'testlist/chapter.html', {'id': id})

def section(request, id):
    return render(request, 'testlist/section.html', {'id': id})

def testcase(request, id):
    return render(request, 'testlist/testcase.html', {'id': id})