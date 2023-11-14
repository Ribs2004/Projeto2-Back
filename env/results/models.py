from django.db import models

class SearchResult(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    probability = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    
