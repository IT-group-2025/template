from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Низкий'),
        ('M', 'Средний'),
        ('H', 'Высокий'),
    ]

    name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_priority_display()})"
