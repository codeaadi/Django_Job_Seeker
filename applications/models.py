from django.db import models
from django.conf import settings
from companies.models import Company

class Application(models.Model):
    STATUS_CHOICES =[
        ('applied','Applied'),
        ('interview','Interview'),
        ('offer','Offer'),
        ('rejected','Rejected'),
    ]
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    
    Company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    position = models.CharField(max_length=150)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='applied')
    
    job_link = models.URLField(blank=True,null=True)
    salary_range = models.CharField(max_length=100,blank=True)
    
    applied_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.position} - {self.company.name}"