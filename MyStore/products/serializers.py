from products.models import *
from rest_framework import serializers
from users.models import User



class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=128)
    description = serializers.CharField()
    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance




class ModelCategorySerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'image')






class ModelProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    comments = UserSerializer(many = True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quontity', 'category', 'category_name','is_active', 'rating_value', 'rating_count', 'comments')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.quontity = validated_data.get('quontity', instance.quontity)
        instance.category = validated_data.get('category', instance.category)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.rating_value = validated_data.get('rating_value', instance.rating_value)
        instance.rating_count = validated_data.get('rating_count', instance.rating_count)

        # Сохраняем изменения в экземпляре Product
        instance.save()

        return instance





    # def create(self, validated_data):
    #     product = Product.objects.create(**validated_data)
    #     return product



# class ModelCommentSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     product = ModelProductSerializer(read_only=True)
#     class Meta:
#         model = Comment
#         fields = ('id', 'user', 'product', 'content', 'commment_date')
