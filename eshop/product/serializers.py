from rest_framework import serializers
from .models import *


# class ProductSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Product
#         fields = "__all__"
#         # fields = ('name','price')

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"

        
class ProductImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImages
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):

    images = ProductImagesSerializer(many=True, read_only=True)
    reviews = serializers.SerializerMethodField(method_name='get_reviews',read_only=True)

    class Meta:
        model = Product
        fields = ('id','name','description','price','brand','category','ratings','reviews','stock','user','images')

        extra_kwargs = {
            "name": {"required": True, 'allow_blank':False},
            "brand": {"required": True, 'allow_blank':False},     
        }   

    def get_reviews(self,obj):
        reviews = obj.reviews.all()
        serializer = ReviewSerializer(reviews,many=True)
        return serializer.data