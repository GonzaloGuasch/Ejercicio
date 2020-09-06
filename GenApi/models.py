from django.db import models


class Disease(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Gen(models.Model):
    chromosome_number = models.CharField(max_length=2)
    chromosome_initial_position = models.IntegerField()
    chromosome_last_position = models.IntegerField()
    symbol = models.CharField(max_length=20)
    diseases = models.ManyToManyField(Disease)

    def __str__(self):
        return self.symbol


class Variant(models.Model):
    chromosome_number = models.CharField(max_length=2)
    position = models.IntegerField()
    id_variant = models.CharField(max_length=10)
    reference = models.CharField(max_length=20, null=True, blank=True)
    alternative = models.CharField(max_length=20, null=True, blank=True)
    gen_symbol = models.ForeignKey(Gen, on_delete=models.CASCADE)

    def __str__(self):
        return self.id







