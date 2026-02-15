from django.db import models
from authenticate.models import User
from core.models import TimeStampMixin


class Activity(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Вид отдыха'
        verbose_name_plural = 'Виды отдыха'


class UserProfile(TimeStampMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    budget_min = models.PositiveIntegerField()
    budget_max = models.PositiveIntegerField(null=True)
    activity = models.ManyToManyField(
        Activity,
        through='ProfileActivity',
        related_name='profile',
        blank=True
    )

    # visa
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class ProfileActivity(models.Model):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE
    )
    priority = models.PositiveSmallIntegerField(default=1)
