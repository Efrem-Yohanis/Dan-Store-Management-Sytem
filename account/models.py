from django.db import models

class new_form1(models.Model):
    First_Name=models.CharField(max_length=200,null=True,blank=True)
    Last_Name=models.CharField(max_length=200,null=True,blank=True)
    Emila=models.CharField(max_length=200,null=True,blank=True)
    Address=models.CharField(max_length=200,null=True,blank=True)
    phone1 = models.CharField(max_length=200, null=True)
    phone2 = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=20,null=True,blank=True)
    profile_pic=models.ImageField(null=True,blank=True, upload_to='Profile/')
class new_form2(models.Model):
    First_Name=models.CharField(max_length=200,null=True,blank=True)
    Last_Name=models.CharField(max_length=200,null=True,blank=True)
    Emila=models.CharField(max_length=200,null=True,blank=True)
    Address=models.CharField(max_length=200,null=True,blank=True)
    phone1 = models.CharField(max_length=200, null=True)
    phone2 = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=20,null=True,blank=True)
    profile_pic=models.ImageField(null=True,blank=True, upload_to='Profile/')
    Titel = models.CharField(max_length=20,null=True,blank=True)
    Filed_Study = models.CharField(max_length=20,null=True,blank=True)
    Collage = models.CharField(max_length=20,null=True,blank=True)
    grade=models.CharField(max_length=20,null=True,blank=True)
    Year_Graguation = models.DateField(null=True,blank=True)
    Document=models.FileField(null=True,blank=True,upload_to="File/Document")

class unAproved_employees(models.Model):
    First_Name=models.CharField(max_length=200,null=True,blank=True)
    Last_Name=models.CharField(max_length=200,null=True,blank=True)
    Emila=models.CharField(max_length=200,null=True,blank=True)
    Address=models.CharField(max_length=200,null=True,blank=True)
    phone1 = models.CharField(max_length=200, null=True)
    phone2 = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=20,null=True,blank=True)
    profile_pic=models.ImageField(null=True,blank=True, upload_to='Profile/')
    Titel = models.CharField(max_length=20,null=True,blank=True)
    Filed_Study = models.CharField(max_length=20,null=True,blank=True)
    Collage = models.CharField(max_length=20,null=True,blank=True)
    grade=models.CharField(max_length=20,null=True,blank=True)
    Year_Graguation = models.DateField(null=True,blank=True)
    Document=models.FileField(null=True,blank=True,upload_to="File/Document")
    Branch=models.CharField(max_length=20,null=True,blank=True)
    Department=models.CharField(max_length=20,null=True,blank=True)
    role=models.CharField(max_length=20,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    cheek=models.BooleanField(null=True,blank=True)
  