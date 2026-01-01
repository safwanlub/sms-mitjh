from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('kepsek', 'Kepala Sekolah'),
        ('guru', 'Guru'),
        ('tu', 'Tata Usaha'),
        ('bendahara', 'Bendahara'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='guru'   # ⬅️ penting!
    )

    REQUIRED_FIELDS = ['email', 'role']

    def __str__(self):
        return f"{self.username} ({self.role})"
