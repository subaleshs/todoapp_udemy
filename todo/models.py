from django.db import models

class List(models.Model):
    job = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.job
