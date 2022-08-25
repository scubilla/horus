from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from app.core.erp.models import Category
from app.core.erp.forms import CategoryForm

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
        data = {}
        # controlar el codig de error del jquery del ajax por una excepcion con try cathc
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
           # cat = Category.objects.get(pk=request.POST['id']).toJSON()
           # data['name'] = cat.name  --> por usar tojson
        except Exception as e:
            data['error'] = str(e)
#        cat = Category.objects.get(pk=request.POST['id'])
#        data['name'] = cat.name
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorias'
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    # redireccionar luego de grabar
    success_url = reverse_lazy('erp:category_list')

    # volvemos a sobreescribir el metodo post
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action =='add':
                form = self.get_form()
                data = form.save()

            else:
                 data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Categoria'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorias'
        context['action'] = 'add'
        return context

