from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    info = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
    
    def get_full_name(self):
        return self.name
    
    class Meta:
        ordering = ['-date_added']
    
