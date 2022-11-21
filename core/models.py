from django.db import models

# Create your models here.


class Music(models.Model):
        name = models.FileField(upload_to="music")
        created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name
