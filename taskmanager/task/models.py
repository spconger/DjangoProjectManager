from django.db import models
from  django.contrib.auth.models import User
import datetime

# Create your models here.

class ProjectType(models.Model):
    typename=models.CharField(max_length=255)

    def __str__(self):
        return self.typename
    
    class Meta:
        db_table='projecttype'

class ProjectDef(models.Model):
    projectname=models.CharField(max_length=255)
    projectType_id = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    startdate=models.DateTimeField()
    projectowner_id=models.ForeignKey(User, on_delete=models.CASCADE)
    projectdescription = models.TextField()

    def __str__(self):
        return self.projectname
    
    class Meta:
        db_table='project'

class WorkLog(models.Model):
    project_id=models.ForeignKey(ProjectDef, on_delete=models.CASCADE)
    start=models.DateTimeField()
    end=models.DateTimeField()
    workdescription=models.CharField(max_length=255)

    def __str__(self):
        return self.workdescription
    
    def CalculateTime(self):
        time1=self.start
        time2=self.end
        delta = time2-time1
        return delta

    class Meta:
        db_table='worklog'



