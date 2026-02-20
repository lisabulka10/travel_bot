from django.db import models


class VisaType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип визы'
        verbose_name_plural = 'Типы визы'


class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.PositiveIntegerField()
    budget = models.PositiveIntegerField()
    climate = models.CharField(max_length=100)
    activities = models.ManyToManyField(
        'profiles.Activity',
        blank=True
    )
    visa = models.ManyToManyField(
        VisaType,
        through='CountryVisa',
        related_name='countries'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class CountryVisa(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_visa')
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name='country_visa')
    visa_required = models.BooleanField(default=False)
