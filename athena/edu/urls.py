from rest_framework import routers

from .views import StudentGroupViewSet, SubjectViewSet

router = routers.DefaultRouter()
router.register("subjects", SubjectViewSet)
router.register("student-groups", StudentGroupViewSet)

urlpatterns = router.urls
