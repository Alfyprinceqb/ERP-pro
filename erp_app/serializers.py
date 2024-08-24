from rest_framework import serializers
from .models import*

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'role_id', 'first_name', 'middle_name', 'last_name', 'mobile', 'email', 'password', 'registered_at', 'last_login', 'introduction','address']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role_id=validated_data['role_id'],
            mobile=validated_data['mobile'],
            introduction=validated_data['introduction'],
            address=validated_data['address']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_category
        fields = '__all__'  

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'              