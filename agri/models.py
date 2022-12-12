from django.db import models

# Create your models here.
class Hudud(models.Model):
    viloyat = models.CharField(max_length=250)

    def __str__(self):
        return self.viloyat

class Tuman(models.Model):
    viloyat = models.ForeignKey(Hudud, null=True, on_delete=models.RESTRICT)
    tuman = models.CharField(max_length=250)

    def __str__(self):
        return self.tuman


class AgriSelect(models.Model):
    tuman = models.ForeignKey(Tuman, null=True, on_delete=models.RESTRICT)
    agri = models.CharField(max_length=250)
    chorva = models.CharField(max_length=250)
    yer = models.IntegerField()
    mahsulot_name =models.CharField(max_length=250)
    mahsulot_soni = models.IntegerField()
    shartnoma = models.CharField(max_length=250)
    ekspert = models.IntegerField()
    bozorga_chaqirishi = models.IntegerField()

    def __str__(self):
        return self.agri


