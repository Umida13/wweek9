
from django.urls import path

from apps.product.serializers import CategorySerializer
from .views import CategoryView, CategoryListView


#http://127/.0.0.1:8000/api/v1/product/create/category    ----> urlpatterns

urlpatterns = [

    path("lists/category/", CategoryListView.as_view()),
    path("create/category/", CategoryView.as_view())
]
