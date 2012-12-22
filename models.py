from django.db import models
from django.utils import timezone
import datetime

class Haber(models.Model):
    baslik= models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    aciklama = models.TextField()
    icerik = models.TextField()
    yay_tarihi=models.DateTimeField('yayinlanma tarihi')
    def __unicode__(self):
        return self.baslik
    def en_son_yayinlanan(self):
        return self.yay_tarihi >= timezone.now() - datetime.timedelta(days=1)
    en_son_yayinlanan.admin_order_field = 'yay_tarihi'
    en_son_yayinlanan.boolean = True
    en_son_yayinlanan.short_description = 'Yeni mi yayinlanandi?'

class Resim(models.Model):
    haber = models.ForeignKey(Haber)
    aciklama = models.CharField(max_length=200)
    resim = models.ImageField(upload_to='haber/%Y/%m/%d')
    def __unicode__(self):
        return self.aciklama
