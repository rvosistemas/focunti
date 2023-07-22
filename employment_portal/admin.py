from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import ApplicantUser

admin.site.register(ApplicantUser, UserAdmin)
