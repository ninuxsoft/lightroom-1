from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Light(models.Model):
    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)
    intensity = models.IntegerField(default=0)

    MIN_INTENSITY = 0
    MAX_INTENSITY = 255

    def __unicode__(self):
        return '(%s,%s)->%s' % (self.pos_x, self.pos_y, self.intensity)

    def toggle(self):
        self.intensity = Light.MAX_INTENSITY - self.intensity
        return self

    def clean(self):
        if self.intensity < Light.MIN_INTENSITY:
            raise ValidationError('Intensity can\'t be less than: %d' % Light.MIN_INTENSITY)
        if self.intensity > Light.MAX_INTENSITY:
            raise ValidationError('Intensity can\'t exceed: %d' % Light.MAX_INTENSITY)
