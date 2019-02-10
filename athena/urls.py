"""athena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication.urls import auth_router
from edu.urls import edu_router
from works.urls import works_router


class ContainerRouter(DefaultRouter):
    """Router class that collect all urls from other apps routers"""

    def register_router(self, router):
        self.registry.extend(router.registry)


root_router = ContainerRouter()
root_router.register_router(auth_router)
root_router.register_router(edu_router)
root_router.register_router(works_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('works.urls')),
]

urlpatterns += root_router.urls
