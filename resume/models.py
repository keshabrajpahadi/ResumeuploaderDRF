from django.db import models
state_choices=((
    ("pradesh1","koshi"),
    ("pradesh2","koshi"),
    ("pradesh3","koshi"),
    ("pradesh4","koshi"),
    ("pradesh5","koshi"),
    ("pradesh6","koshi"),
    ("pradesh7","koshi"),
))

# Create your models here.
class Profile(models.Model):
    name=models.CharField()
    email=models.EmailField()
    dob=models.DateField(auto_now=False,auto_now_add=False)
    state=models.CharField(choices=state_choices,max_length=50)
    gender=models.CharField()
    location=models.CharField()
    profile_image=models.ImageField(upload_to='pimages',blank=True)
    document=models.FileField(upload_to='rdocs',blank=True)


