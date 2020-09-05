from django.db import models


class Disease(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name


class Variant(models.Model):
    chromosome_number = models.CharField(max_length=2)
    position = models.IntegerField()
    id = models.CharField(max_length=10, primary_key=True)
    reference = models.CharField(max_length=20, null=True, blank=True)
    alternative = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.id


class Gen(models.Model):
    chromosome_number = models.CharField(max_length=2)
    chromosome_initial_position = models.IntegerField()
    chromosome_last_position = models.IntegerField()
    symbol = models.CharField(max_length=20, primary_key=True, blank=True)
    related_disease = models.ManyToManyField(Disease, blank=True)
    gen = models.ForeignKey(Variant, related_name='gen_symbol', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('gen', 'symbol')

    def __str__(self):
        return self.symbol


