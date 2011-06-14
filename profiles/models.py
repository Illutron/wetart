from django.db import models
from sorl.thumbnail import ImageField

class Profile(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    image = ImageField(
        upload_to='images/profiles/',
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.name