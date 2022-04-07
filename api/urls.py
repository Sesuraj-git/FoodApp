from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import *

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('customers', CustomerViewSet)
router.register('menu', MenuViewSet)
# router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]