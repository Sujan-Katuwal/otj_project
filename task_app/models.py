from django.db import models
from custom_user.models import CustomUser

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    STATUS_CHOICE = [
        ('not started', 'not started'),
        ('in progress', 'in progress'),
        ('completed', 'completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='not started')
    assign_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
    


    

    
