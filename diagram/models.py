from django.db import models

class QalaData(models.Model):
    qala= models.CharField(max_length=100)
    halyq = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Qala Halyq bazasy'

    def __str__(self):
        return f'{self.qala}-{self.halyq}'
