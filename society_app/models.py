from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import UserManager
class CustomUserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)

class Member(AbstractUser):
    objects = CustomUserManager()
    username = models.CharField(max_length=10, primary_key=True, unique=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField(null=True)
    active_status = (
        ('A','Active'),
        ('U','Unactive'),
        ('S','Suspended'),
    )
    commitee = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    commitee_member = models.CharField(max_length=1, choices=commitee, default='N')
    status = models.CharField(max_length=1, choices=active_status, default='A')
    password = models.CharField(max_length=50)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Complaint(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=(('O', 'Open'), ('C', 'Closed')), default='O')

    def __str__(self):
        return self.title

class MaintenanceRecord(models.Model):
    title = models.CharField(max_length=100, default="February")
    cost = models.DecimalField(max_digits=8, decimal_places=2, default=500)
    date = models.DateField(auto_now_add=True)
    pay_date = models.DateTimeField(null=True, blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.member.username
    
