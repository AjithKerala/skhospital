from django.db import models

# Create your models here.
class departmentss(models.Model):
    image=models.ImageField(upload_to='department')
    depart=models.CharField(max_length=100)
    def __str__(self):
        return self.depart
