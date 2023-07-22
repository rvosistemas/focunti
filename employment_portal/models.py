from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


# Create your models here.
class ApplicantUser(AbstractUser):
    identification_number = models.CharField(max_length=20, unique=True)
    profile_description = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return self.username

    def get_full_name(self) -> str:
        return self.username + " " + self.last_name


class Company(models.Model):
    name = models.CharField(max_length=100)
    nit = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="offers")
    skills = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Postulation(models.Model):
    user = models.ForeignKey(ApplicantUser, on_delete=models.CASCADE, related_name="postulations")
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="postulations")

    def __str__(self) -> str:
        return f"{self.user.username} - {self.offer.title}"
