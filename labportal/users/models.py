from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('lab_assistant', 'Lab Assistant'),        
    ]

    # Already inherited:
    # first_name, last_name, email, password, is_active, is_staff, is_superuser, username

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student'
    )

    def save(self, *args, **kwargs):
        # Auto-generate a unique username from first + last name if not provided
        if not self.username and self.first_name and self.last_name:
            base_username = f"{self.first_name.lower()}.{self.last_name.lower()}"
            username = base_username
            counter = 1
            # Ensure uniqueness
            while CustomUser.objects.filter(username=username).exclude(pk=self.pk).exists():
                username = f"{base_username}{counter}"
                counter += 1
            self.username = username

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
