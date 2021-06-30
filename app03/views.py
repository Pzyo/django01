from django.shortcuts import render,HttpResponse,reverse

# Create your views here.
def reg(request):
    # print(reverse('ggg'))
    # print(reverse('app03:ggg'))
    print(reverse('app03_ggg'))
    return HttpResponse('app03/reg')