from rest_framework import routers

from .views import StudentGroupViewSet, SubjectViewSet, SpecialityViewSet

router = routers.DefaultRouter()
router.register("subjects", SubjectViewSet)
router.register("specialities", SpecialityViewSet)
router.register("student-groups", StudentGroupViewSet)

urlpatterns = router.urls
