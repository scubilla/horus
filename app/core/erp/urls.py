from django.urls import path

from app.core.erp.views import myFirstView, mySecondView

app_name = 'erp'

urlpatterns = [
    path('uno/', myFirstView, name='vista1'),
    path('dos/', mySecondView, name='vista2')
]
