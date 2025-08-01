from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ConsoleListing(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    console_name=models.CharField(max_length=60)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    location=models.CharField(max_length=100)
    available=models.BooleanField(default=True)
    photo1=models.ImageField(upload_to='console_photos/',null=False,blank=False)
    photo2=models.ImageField(upload_to='console_photos/',null=False,blank=False)
    posted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.console_name}"





