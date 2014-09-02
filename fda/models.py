from django.db import models

# Create your models here.

class ExpertStatement(models.Model):
    foodName  = models.CharField(max_length=200)
    statement  = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
    	return self.foodName


