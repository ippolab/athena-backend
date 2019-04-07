from django.urls import path
from rest_framework import routers

from .views import TokenView, RoleViewSet, StudentViewSet, TeacherViewSet, TutorViewSet, UserViewSet, \
    get_profile_view

router = routers.DefaultRouter()
router.register("roles", RoleViewSet)
router.register("users", UserViewSet)
router.register("students", StudentViewSet)
router.register("tutors", TutorViewSet)
router.register("teachers", TeacherViewSet)

urlpatterns = [
    path("login/", TokenView.as_view(), name="login"),
    path("profile/me/", get_profile_view, name="profile")
]

urlpatterns += router.urls
