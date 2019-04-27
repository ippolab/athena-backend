from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    RoleViewSet,
    StudentViewSet,
    TeacherViewSet,
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
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="verify"),
    path("profile/me/", get_profile_view, name="profile"),
]

urlpatterns += router.urls
