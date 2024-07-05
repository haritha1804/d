from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    TEACHER = 'teacher'
    STUDENT = 'student'
    ROLE_CHOICES = [
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    ]
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change the related name here
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Change the related name here
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.student.username} - {self.subject.name}'
