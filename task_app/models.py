from django.db import models
from datetime import datetime 

class Project(models.Model):
    
    name = models.CharField(max_length=20,null=False)
    
    def __str__(self):
        
        return self.name
    
class Customer(models.Model):
    
    name = models.CharField(max_length=25,null=False)
        
    def __str__(self):
        return self.name
    
class Status(models.Model):
    
    title = models.CharField(max_length=20,null=False)
        
    def __str__(self):
        return self.title
    
class Task(models.Model):
    
    title = models.CharField(max_length=100,null=False)
    project = models.ForeignKey(Project,max_length=50,on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(Status,max_length=20,on_delete=models.CASCADE, null=True)
    details = models.TextField(null=False)
    creation = models.DateTimeField(default= datetime.now, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    