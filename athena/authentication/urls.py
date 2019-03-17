from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from django.urls import path

from .views import (
    CustomTokenObtainPairView,
    StudentViewSet,
    TeacherViewSet,
    TutorViewSet,
)

router = routers.DefaultRouter()
router.register("students", StudentViewSet)
router.register("tutors", TutorViewSet)
router.register("teachers", TeacherViewSet)

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name='login'),
    path("token-refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
