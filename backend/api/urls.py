from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, StudentViewSet, ThesisViewSet,
    ArticleViewSet, ProgressReportViewSet, RequestViewSet,
    MeetingViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet, basename='student')
router.register(r'theses', ThesisViewSet, basename='thesis')
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'progress-reports', ProgressReportViewSet, basename='progress-report')
router.register(r'requests', RequestViewSet, basename='request')
router.register(r'meetings', MeetingViewSet, basename='meeting')

urlpatterns = [
    path('', include(router.urls)),
]