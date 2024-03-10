from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class PawUser(AbstractUser):
    profile_picture = models.ImageField(
        upload_to='profile_pics/', null=True, blank=True)
    language = models.CharField(max_length=2, default='en')
    telegram_username = models.CharField(max_length=50, null=True, blank=True)
    use_darkmode = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class GoogleSSOUser(models.Model):
    paw_user = models.OneToOneField(
        PawUser, on_delete=models.CASCADE, primary_key=True)
    google_id = models.CharField(max_length=255)

    def __str__(self):
        return self.paw_user.username

    class Meta:
        db_table = "google_sso_user"
        verbose_name = _("Google SSO User")
