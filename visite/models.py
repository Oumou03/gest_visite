from django.db import models
from django.utils import timezone

class Visit(models.Model):
    PURPOSE_CHOICES = [
        ('REUNION', 'Réunion'),
        ('LIVRAISON', 'Livraison'),
        ('MAINTENANCE', 'Maintenance'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'En attente'),
        ('ONGOING', 'En cours'),
        ('COMPLETED', 'Terminé'),
    ]

    # Champs principaux
    visitor_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    host_person = models.CharField(max_length=100)
    
    # Nouveaux champs (Contact & Signature)
    phone_number = models.CharField(max_length=20, default="")
    email = models.EmailField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True) 

    # Status et temps
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, default='REUNION')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    # Remplace la ligne arrival_time par celle-ci :
    arrival_time = models.DateTimeField(default=timezone.now)
    departure_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.visitor_name