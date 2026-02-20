from django.db import models
from authenticate.models import User
from core.models import TimeStampMixin


class Activity(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид отдыха'
        verbose_name_plural = 'Виды отдыха'


class UserProfile(TimeStampMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profiles'
    )
    budget_min = models.PositiveIntegerField(blank=True, null=True)
    budget_max = models.PositiveIntegerField(blank=True, null=True)
    activities = models.ManyToManyField(
        Activity,
        through='ProfileActivity',
        related_name='profiles',
        blank=True,
        null=True
    )
    visa = models.ManyToManyField(
        'countries.VisaType',
        through='ProfileVisa',
        related_name='profiles',
        blank=True,
    )

    def __str__(self):
        return str(self.user)

    # visa
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class ProfileActivity(models.Model):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='profile_activity'
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name='profile_activity'
    )
    priority = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ('priority',)


class ProfileVisa(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='profile_visa')
    visa = models.ForeignKey('countries.VisaType', on_delete=models.CASCADE, related_name='profile_visa')
