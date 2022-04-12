from django.shortcuts import render
from app.core.erp.models import Category

# lista basada en un afuncion
def category_list(request):
    data = {
        'title': 'Listado de Categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)
