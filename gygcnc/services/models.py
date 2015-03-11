from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=70)
    img = models.ImageField(upload_to='services_img')
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
