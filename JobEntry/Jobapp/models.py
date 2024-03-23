from django.db import models



# Create your models here.

class Job(models.Model):
    CAT=((1,"Human Resource"),(2,"Business Development"),(3,"Marketing"))
    cat = models.IntegerField(verbose_name="Category",choices=CAT)
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    published_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_active = models.BooleanField(default=True, verbose_name="Available")
    p_img=models.ImageField(upload_to="image")
   

    # def __str__(self):
    #     return self.title