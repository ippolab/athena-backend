from rest_framework import routers

from .views import SubjectViewSet, StudentGroupViewSet

edu_router = routers.DefaultRouter()
edu_router.register('subjects', SubjectViewSet)
edu_router.register('student-groups', StudentGroupViewSet)
