from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Service(models.Model):

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=900)
    image = models.ImageField(null=True, blank=True)

    is_stay = models.BooleanField(default=False)
    no_of_guests = models.IntegerField(null=True, blank=True)
    has_breakfast = models.BooleanField(default=True, null=True, blank=True)

    is_relax = models.BooleanField(default=False)
    length = models.IntegerField(null=True, blank=True)
    scents = models.CharField(max_length=254, null=True, blank=True)

    is_eat = models.BooleanField(default=False)
    protein = models.CharField(max_length=254, null=True, blank=True)
    no_of_courses = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
