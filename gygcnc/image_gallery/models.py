from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from model_utils.models import TimeStampedModel


class Gallery(TimeStampedModel):

    product = models.ForeignKey('products.Product',
                                related_name="galleries",
                                blank=True, null=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Photo(TimeStampedModel):

    gallery = models.ForeignKey(Gallery, related_name='photos')
    image = models.ImageField(upload_to='products_images')

    def __unicode__(self):
        return "%s --> %s" % (self.id, self.gallery)


#  SIGNALS

@receiver(post_delete, sender=Photo)
def photo_post_delete_handler(sender, **kwargs):
    instance = kwargs['instance']
    storage, path = instance.image.storage, instance.image.path
    storage.delete(path)
