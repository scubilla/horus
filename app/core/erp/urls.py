from django.urls import path
from app.core.erp.views.category.views import category_list

#from app.core.erp.views import myFirstView, mySecondView

app_name = 'erp'

urlpatterns = [
    path('category/list/', category_list, name='category_list'),
    #path('dos/', mySecondView, name='vista2')
]
