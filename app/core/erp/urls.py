from django.urls import path

from app.core.erp.views import myFirstView, mySecondView

urlpatterns = [
    path('uno/', myFirstView),
    path('dos/', mySecondView)
]
