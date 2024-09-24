
from django.shortcuts import render
from django.http import HttpResponse

from .tasks import *
from .models import Test
# Create your views here.


def main(request):
    create_test.delay()
    return HttpResponse('created')

def test_list(request):
    tests = Test.objects.all()
    names = ''
    for i in tests:
        names += str(i.name)
    return HttpResponse(f'--{names}')

