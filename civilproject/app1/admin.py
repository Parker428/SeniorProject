from django.contrib import admin
from .models import CompanyReview, CompanyContact


# Register your models here.

admin.site.register(CompanyReview)

admin.site.register(CompanyContact)