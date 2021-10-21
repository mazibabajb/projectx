from django.db import models
from django.urls import reverse

# Create your models here.
class Suburb(models.Model):
    name = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255) 
    description= models.TextField()
    thumbnail = models.FileField()


    def __str__(self):
        return self.name

class Landload(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



     
class Property(models.Model):
    CATEGORY_CHOICES = (
     ('INDUSTRIAL', 'INDUSTRIAL'),
     ('RESIDENTAIL', 'RESIDENTAIL'),
     ('OFFICES', 'OFFICES'),
    )
    url_slug = models.CharField(max_length=255) 
    category = models.CharField(choices = CATEGORY_CHOICES,default= 'RESIDENTAIL',max_length=200)
    price = models.IntegerField(default=0)
    property_description = models.TextField()
    property_img = models.ImageField(upload_to='cars',default='default-car.png') 
    occupation_date = models.DateTimeField(auto_now_add=True)
    property_owner = models.ForeignKey(Landload,on_delete=models.CASCADE)
    prefered_tenant = models.CharField(max_length=200)
    number_of_rooms = models.IntegerField(default=1)
    Suburb = models.ForeignKey(Suburb,on_delete=models.CASCADE)
    condition = models.CharField(max_length=300)
    number_of_beds = models.CharField(max_length=300,blank=True)
    garage = models.CharField(max_length=300,blank=True)
    bath = models.CharField(max_length=300,blank=True)
    is_hot = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("property_detail",args=[self.id])
     


    def __str__(self):
        return self.url_slug

   
