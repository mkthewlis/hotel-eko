from django.db import models


class Stay(models.Model):

    class Meta:
        verbose_name_plural = 'Room types'

    sku = models.CharField(max_length=254, null=True, blank=True)
    item_type = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    no_of_guests = models.IntegerField(null=True, blank=True)
    shower_bath = models.CharField(max_length=254, null=True, blank=True)
    view = models.CharField(max_length=254, null=True, blank=True)
    has_breakfast = models.BooleanField(default=True, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Relax(models.Model):

    class Meta:
        verbose_name_plural = 'Spa treatments'

    sku = models.CharField(max_length=254, null=True, blank=True)
    item_type = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    length = models.IntegerField(null=True, blank=True)
    scents = models.CharField(max_length=254, null=True, blank=True)
    aims = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Eat(models.Model):

    class Meta:
        verbose_name_plural = 'Menu types'

    sku = models.CharField(max_length=254, null=True, blank=True)
    item_type = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    protein = models.CharField(max_length=254, null=True, blank=True)
    no_of_courses = models.IntegerField(null=True, blank=True)
    has_gluten = models.BooleanField(default=True, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
