from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import User, Student, Thesis, Article, ProgressReport, Request, Meeting
from .serializers import (
    UserSerializer, StudentSerializer, ThesisSerializer,
    ArticleSerializer, ProgressReportSerializer, RequestSerializer,
    MeetingSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        if self.request.user.role == 'admin':
            return Student.objects.all()
        elif self.request.user.role == 'advisor':
            return Student.objects.filter(advisor=self.request.user)
        return Student.objects.filter(user=self.request.user)

class ThesisViewSet(viewsets.ModelViewSet):
    serializer_class = ThesisSerializer
    
    def get_queryset(self):
        if self.request.user.role in ['admin', 'advisor']:
            return Thesis.objects.all()
        return Thesis.objects.filter(student__user=self.request.user)

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        if self.request.user.role in ['admin', 'advisor']:
            return Article.objects.all()
        return Article.objects.filter(student__user=self.request.user)

class ProgressReportViewSet(viewsets.ModelViewSet):
    serializer_class = ProgressReportSerializer
    
    def get_queryset(self):
        if self.request.user.role in ['admin', 'advisor']:
            return ProgressReport.objects.all()
        return ProgressReport.objects.filter(student__user=self.request.user)

class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    
    def get_queryset(self):
        if self.request.user.role == 'admin':
            return Request.objects.all()
        elif self.request.user.role == 'advisor':
            return Request.objects.filter(student__advisor=self.request.user)
        return Request.objects.filter(student__user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        request_obj = self.get_object()
        request_obj.status = 'approved'
        request_obj.save()
        return Response({'status': 'request approved'})
    
    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        request_obj = self.get_object()
        request_obj.status = 'rejected'
        request_obj.save()
        return Response({'status': 'request rejected'})

class MeetingViewSet(viewsets.ModelViewSet):
    serializer_class = MeetingSerializer
    
    def get_queryset(self):
        if self.request.user.role == 'advisor':
            return Meeting.objects.filter(advisor=self.request.user)
        return Meeting.objects.filter(student__user=self.request.user)