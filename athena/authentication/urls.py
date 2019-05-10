from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    StudentViewSet,
    TeacherViewSet,
    TutorViewSet,
    UserViewSet,
    get_profile_view,
    set_password_owner_view,
    set_password_admin_view,
)

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("students", StudentViewSet)
router.register("tutors", TutorViewSet)
router.register("teachers", TeacherViewSet)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="verify"),
    path("profile/me/", get_profile_view, name="profile"),
    path("profile/me/password/", set_password_owner_view, name="set-password-owner"),
    path(
        "profile/<str:username>/password/",
        set_password_admin_view,
        name="set-password-admin",
    ),
]

urlpatterns += router.urls
