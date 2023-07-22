from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


# Create your models here.
class ApplicantUser(AbstractUser):
    identification_number = models.CharField(max_length=20, unique=True)
    profile_description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return self.username

    def get_full_name(self) -> str:
        return self.first_name + " " + self.last_name

    groups = models.ManyToManyField(
        Group,
        verbose_name="user groups",
        blank=True,
        related_name="applicant_users",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        related_name="applicant_users",
    )


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
