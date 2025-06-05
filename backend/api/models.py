from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Doctorant'),
        ('advisor', 'Encadrant'),
        ('admin', 'Administrateur'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField()
    research_topic = models.CharField(max_length=255)
    start_date = models.DateField()
    expected_end_date = models.DateField()
    advisor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='supervised_students')
    status = models.CharField(max_length=20, default='active')

class Thesis(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    keywords = models.CharField(max_length=255)
    submission_date = models.DateTimeField(auto_now_add=True)
    defense_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='in_progress')
    document = models.FileField(upload_to='theses/')

class Article(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    journal = models.CharField(max_length=255)
    publication_date = models.DateField()
    status = models.CharField(max_length=20, default='submitted')
    document = models.FileField(upload_to='articles/')

class ProgressReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    period = models.CharField(max_length=20)
    content = models.TextField()
    status = models.CharField(max_length=20, default='submitted')
    document = models.FileField(upload_to='reports/')

class Request(models.Model):
    REQUEST_TYPES = (
        ('registration', 'Inscription'),
        ('extension', 'Dérogation'),
        ('defense', 'Soutenance'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    description = models.TextField()
    document = models.FileField(upload_to='requests/', null=True, blank=True)

class Meeting(models.Model):
    advisor = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(max_length=20, default='scheduled')