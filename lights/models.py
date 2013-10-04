from django.db import models

# Create your models here.
class Light(models.Model):
    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)
    intensity = models.IntegerField(default=0)

    def __unicode__(self):
        return '(%s,%s)->%s' % (self.pos_x, self.pos_y, self.intensity)

    def toggle(self):
        return 100 - self.intensity
