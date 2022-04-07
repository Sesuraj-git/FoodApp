from rest_framework import serializers
from .models import User, Customer, Restaurant, Timings, Menu, Order, Cart
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('user', 'f_name', 'l_name', 'college_id', 'college_mail', 'phone', 'address')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('user', 'rname', 'info', 'min_ord', 'location', 'r_logo', 'status', 'is_approved')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("item_name", "r_id", "price", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('total_amount', 'timestamp', 'delivery_in', 'orderedBy', 'r_id', 'status')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('item_id', 'ord_id', 'quantity', 'cart_total')
