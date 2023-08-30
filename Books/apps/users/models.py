from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(gettext('The email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(gettext("Superuser must have is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(gettext("Superuser must have is_superuser=True"))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(gettext('username'), max_length=150,
                                validators=[AbstractUser.username_validator],
                                null=True, blank=True,)
    email = models.EmailField(gettext('email address'), unique=True)
    is_active = models.BooleanField(gettext('active'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Profile(models.Model):
    username_id = models.OneToOneField(
        CustomUser, related_name="user_profile", on_delete=models.CASCADE,
    )
    bio = models.TextField("О себе", null=True, max_length=1000, blank=True)
    birth_date = models.DateField("День рождение", null=True, blank=True)
    profile_img = models.ImageField(
        "Фото профиля", null=True, blank=True, upload_to="users/profile/"
    )
    country = models.TextField("Страна", max_length=100, null=True, blank=True)
    city = models.TextField("Город", max_length=168, null=True, blank=True)
    phoneNumber = PhoneNumberField("Номер телефона", unique=True, null=True,
                                   blank=True)
    is_phone_verified = models.BooleanField(default=False)
    balance = models.DecimalField(
        "Баланс", max_digits=8, decimal_places=2, blank=True, default=0
    )

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


@receiver(post_save, sender=CustomUser)
def create_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(username_id=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(instance, **kwargs):
    instance.user_profile.save()

