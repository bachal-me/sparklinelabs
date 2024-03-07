from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, default="")
    email_sub = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    Project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=100)
    project_desc = models.CharField(max_length=500)
    project_link = models.CharField(max_length=100, default="")
    project_category = models.CharField(max_length=50, default="")
    pub_date = models.DateField()
    project_image = models.ImageField(upload_to='static/projects/images')

    def __str__(self):
        return self.project_title
