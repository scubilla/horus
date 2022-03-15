from django.urls import path

from app.core.erp.views import myFirstView

urlpatterns = [
    path('uno/', myFirstView),
    path('dos/', myFirstView)
]
