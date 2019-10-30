from django.db import models

# Create your models here.
class web(models.Model):
    integer_field   = models.IntegerField()
    char_field      = models.CharField(max_length=5)
    float_field     = models.FloatField()
    date_field      = models.DateField(auto_now=True)
    date_time_field = models.DateTimeField(auto_now_add=True)
    email           = models.EmailField()
    text            = models.TextField(max_length=20)