from django.shortcuts import render
from django.views.generic import ListView

from app.core.erp.models import Category, Product


# lista basada en un afuncion
def category_list(request):
    data = {
        'title': 'Listado de Categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    # cambiando el query set, sobrescribiendo comportamiento de metodos del get
    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        return context
