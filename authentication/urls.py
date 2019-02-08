from rest_framework import routers

from .views import UserViewSet, GroupViewSet

auth_router = routers.DefaultRouter()
auth_router.register('users', UserViewSet)
auth_router.register('groups', GroupViewSet)
