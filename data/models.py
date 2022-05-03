from statistics import mode
from django.db import models


class Record(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    
    def __str__(self):
        return self.name

class SubRecord(models.Model):
    record = models.ForeignKey(Record, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)