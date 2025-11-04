from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobListingViewSet, ApplicationViewSet

router = DefaultRouter()
router.register(r'jobs', JobListingViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]