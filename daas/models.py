from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField


class User(AbstractUser):
    avatar = ImageField(upload_to='images/', null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'