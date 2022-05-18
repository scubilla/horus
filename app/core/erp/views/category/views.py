from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.utils.decorators import method_decorator

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
    #def get_queryset(self):
    #    return Product.objects.all()

    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        #if request.method == 'GET':
        #   return redirect('erp:category_list2')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # data = {'name': 'Simon'}
        data = {}
        cat = Category.objects.get(pk=request.POST['id'])
        data['name'] = cat.name
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        return context
