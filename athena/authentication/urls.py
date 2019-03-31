from django.urls import path
from rest_framework import routers

from .views import (
    RolesTokenObtainSlidingView,
    RoleViewSet,
    StudentViewSet,
    TeacherViewSet,
    TutorViewSet,
    UserViewSet)

router = routers.DefaultRouter()
router.register("roles", RoleViewSet)
router.register("users", UserViewSet)
router.register("students", StudentViewSet)
router.register("tutors", TutorViewSet)
router.register("teachers", TeacherViewSet)

urlpatterns = [path("login/", RolesTokenObtainSlidingView.as_view(), name="login")]

urlpatterns += router.urls
