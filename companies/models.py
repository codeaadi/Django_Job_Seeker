from django.db import models
from django.conf import settings

class Company(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='companies'
    )
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True,null=True)
    location = models.CharField(max_length=150,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name