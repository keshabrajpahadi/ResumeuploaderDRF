from django.urls import path
from .views import ListProfileApiView


urlpatterns = [
    path('resume/',ListProfileApiView.as_view(),name = "list")
]