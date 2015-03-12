from django.db import models

from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager


class Product(TimeStampedModel):

    name = models.CharField(max_length=100)
    description = models.TextField()
    link_to_sell = models.URLField()
    available = models.BooleanField(default=True)

    categories = TaggableManager()

    def __unicode__(self):
        return self.name

