from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def testcase(request):
    testcases = Testcase.objects.all()
    return render(request, 'testlist/testcase.html', {'testcases': testcases})
