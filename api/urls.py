from django.urls import path

from .views import SignUpView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SubjectViewSet, MarkViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'marks', MarkViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("signup/", SignUpView.as_view(), name="signup"),
]
