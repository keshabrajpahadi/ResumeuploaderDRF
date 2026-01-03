from django.db import models
state_choices = (
    ("pradesh1", "Koshi Pradesh"),
    ("pradesh2", "Madhesh Pradesh"),
    ("pradesh3", "Bagmati Pradesh"),
    ("pradesh4", "Gandaki Pradesh"),
    ("pradesh5", "Lumbini Pradesh"),
    ("pradesh6", "Karnali Pradesh"),
    ("pradesh7", "Sudurpashchim Pradesh"),
)

# Create your models here.
class Profile(models.Model):
    name=models.CharField()
    email=models.EmailField()
    dob=models.DateField(auto_now=False,auto_now_add=False)
    state=models.CharField(choices=state_choices,max_length=50)
    gender=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    location=models.CharField()
    profile_image=models.ImageField(upload_to='pimages',blank=True)
    document=models.FileField(upload_to='rdocs',blank=True)


