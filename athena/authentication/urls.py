from rest_framework import routers
from django.urls import path

from .views import (
    RolesTokenObtainSlidingView,
    StudentViewSet,
    TeacherViewSet,
    TutorViewSet,
)

router = routers.DefaultRouter()
router.register("students", StudentViewSet)
router.register("tutors", TutorViewSet)
router.register("teachers", TeacherViewSet)

urlpatterns = [
    path("login/", RolesTokenObtainSlidingView.as_view(), name='login'),
]

urlpatterns += router.urls
