from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, tg_id, **extra_fields):
        if not tg_id:
            raise ValueError('Telegram ID id required')
        user = self.model(tg_id=tg_id, **extra_fields)
        user.save(using=self._db)
        return user

    # createsuperuser


class User(AbstractUser):
    tg_id = models.PositiveBigIntegerField(
        verbose_name='Telegram ID',
        blank=True,
        null=False,
        unique=True
    )
    username = models.CharField(
        verbose_name='Username',
        max_length=255,
        blank=True,
        null=True,
        default='',
        unique=False
    )
    first_name = models.CharField(
        verbose_name='First name',
        max_length=255,
        blank=True,
        null=True,
        default='',
        unique=False
    )
    last_name = models.CharField(
        verbose_name='Last name',
        max_length=255,
        blank=True,
        null=True,
        default='',
        unique=False
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    )

    objects = UserManager

    USERNAME_FIELD = 'tg_id'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username or self.tg_id}'

    class Meta:
        ordering = ('tg_id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
