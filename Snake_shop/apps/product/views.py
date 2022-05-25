


from os import stat
from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer

from .models import Category

#FBV - function base view (decorator)
#CBV - class base view (APIView, generics, ModelViewSet)
# GET PUT POST DELETE
 

class CategoryView(APIView):

    def post(self, request):
        post = request.POST
        print(post)
        serializer = CategorySerializer(data=post)  #data-argument (POST, PUT, PUTCH)
        if serializer.is_valid(raise_exception=True):
            Category.objects.create(**serializer.validated_data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)


    # def get(self, request):
    #     category = Category.objects.all() #QuerySet[]
    #     serializer = CategorySerializer(category, many=True)
    #     data = serializer.data
    #     return Response(data, status=status.HTTP_200_OK)



class CategoryListView(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


