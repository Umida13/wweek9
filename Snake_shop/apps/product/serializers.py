from rest_framework import serializers
from .models import Category

# class CategorySerializer(serializers.Serializer):


#     title = serializers.CharField(max_length=150)
#     slug = serializers.SlugField(max_length= 150)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', 'slug')
