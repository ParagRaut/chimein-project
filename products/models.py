from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    votes_total = models.IntegerField(default=1)
    icon = models.ImageField(upload_to="images/")
    image = models.ImageField(upload_to="images/")
    body = models.TextField(blank=False)
    chimer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return(self.title)

    def summary(self):
        if(len(self.body) > 150):
            return self.body[:150] + "..."

    def __unicode__(self):
        pass
