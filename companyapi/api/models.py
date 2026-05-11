from django.db import models

# Create your models here.

#create company model
class company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('It','It'),('Non IT','Non It'),('Mobile Phone','Mobile Phone')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    #comapny nu name jova mate
    def __str__(self):
          return self.name + '-' +self.location

#Employee model
class Employee(models.Model):
        name=models.CharField(max_length=100)
        email=models.CharField(max_length=100)
        address=models.CharField(max_length=200)
        phone=models.CharField(max_length=10)
        about=models.TextField()
        position=models.CharField(max_length=50,choices=(('Manager','Manager'),('software devloper','sd'),('project leader','pl')))

        company=models.ForeignKey(company,on_delete=models.CASCADE)