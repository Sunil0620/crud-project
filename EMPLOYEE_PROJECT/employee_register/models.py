from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50) 

    def __str__(self):
        return str(self.title)
    
class Employee(models.Model):
    full_name = models.CharField(max_length= 100)
    employee_code = models.CharField(max_length= 3)
    mobile_number = models.CharField(max_length= 15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
