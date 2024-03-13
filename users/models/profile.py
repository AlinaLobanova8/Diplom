
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        'users.User', models.CASCADE, related_name='profile',
        verbose_name='User', primary_key=True,
    )
    telegram_id = models.CharField(
        'Telegram ID', max_length=20, null=True, blank=True
    )

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'Users profile'

    def __str__(self):
        return f'{self.user} ({self.pk})'