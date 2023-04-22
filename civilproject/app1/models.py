from django.db import models

# Create your models here.

class CompanyReview(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    message = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.message

class CompanyContact(models.Model):
    fname = models.CharField(max_length=30, null=False, blank=False)
    lname = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    message = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.fname