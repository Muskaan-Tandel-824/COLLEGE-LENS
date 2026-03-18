from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('college_admin', 'College Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    # Add other student-specific fields here if needed
    
    def __str__(self):
        return f"{self.user.username} Profile"

class CollegeAdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='college_profile')
    college = models.ForeignKey('colleges.College', on_delete=models.CASCADE, related_name='admins')
    
    def __str__(self):
        return f"{self.user.username} - {self.college.name} Admin"
