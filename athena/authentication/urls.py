from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshSlidingView, TokenVerifyView

from .views import (
    RoleViewSet,
    StudentViewSet,
    TeacherViewSet,
    TokenView,
    TutorViewSet,
    UserViewSet,
    get_profile_view,
)

router = routers.DefaultRouter()
router.register("roles", RoleViewSet)
router.register("users", UserViewSet)
router.register("students", StudentViewSet)
router.register("tutors", TutorViewSet)
router.register("teachers", TeacherViewSet)

urlpatterns = [
    path("login/", TokenView.as_view(), name="login"),
    path("login/refresh/", TokenRefreshSlidingView.as_view(), name="refresh"),
    path("login/verify/", TokenVerifyView.as_view(), name="refresh"),
    path("profile/me/", get_profile_view, name="profile"),
]

urlpatterns += router.urls
