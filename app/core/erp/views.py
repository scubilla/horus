from django.shortcuts import render

#from django.http import HttpResponse, JsonResponse
# Create your views here.

def myFirstView(request):
    data = {
        'name': 'Simon'
    }
#    return JsonResponse(data)
    return render(request, 'index.html',data)