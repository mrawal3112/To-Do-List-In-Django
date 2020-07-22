from django.db import models

# Create your models here.
class listdb(models.Model):
    Activity = models.CharField(max_length=50)
    Done = models.BooleanField(default=False)
    Complete = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Activity
