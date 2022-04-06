from django.shortcuts import render

#from django.http import HttpResponse, JsonResponse
# Create your views here.
from app.core.erp.models import Category, Product


def myFirstView(request):
    data = {
        'name': 'Simon',
        'categories': Category.objects.all()
    }
#    return JsonResponse(data)
    return render(request, 'home.html',data)


def mySecondView(request):
    data = {
        'name': 'Simon',
        'products': Product.objects.all()
    }
#    return JsonResponse(data)
    return render(request, 'second.html',data)