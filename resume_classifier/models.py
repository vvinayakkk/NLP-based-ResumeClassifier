from django.db import models

# Create your models here.
from django.db import models

class Resume(models.Model):
    category = models.CharField(max_length=255)
    resume_text = models.TextField()

    def __str__(self):
        return self.category
