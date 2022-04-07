from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, Customer, Restaurant, Timings, Menu, Order, Cart
from .serializers import UserSerializer, CustomerSerializer, RestaurantSerializer, MenuSerializer, OrderSerializer, \
    CartSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        ord_id = request.data['orderid']
        select = request.data['orderstatus']
        select = int(select)
        order = Order.objects.filter(ord_id=ord_id)
        if len(order):
            x = Order.ORDER_STATE_WAITING
            if select == 1:
                x = Order.ORDER_STATE_PLACED
            elif select == 2:
                x = Order.ORDER_STATE_ACKNOWLEDGED
            elif select == 3:
                x = Order.ORDER_STATE_COMPLETED
            elif select == 4:
                x = Order.ORDER_STATE_DISPATCHED
            elif select == 5:
                x = Order.ORDER_STATE_CANCELLED
            else:
                x = Order.ORDER_STATE_WAITING
            order[0].status = x
            order[0].save()

    def list(self, request, *args, **kwargs):
        user = request.user
        user = User.objects.get(username=user)
        serializer = OrderSerializer(orderedBy=user)
        print('order')
        response = {'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        print(user)
        serializer = MenuSerializer(many=True)
        response = {'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)
