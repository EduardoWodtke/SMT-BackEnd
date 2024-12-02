"""
Database models.
"""

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from uploader.models import Image

from .categoria import Categoria


class UserManager(BaseUserManager):
    """Manager for users."""

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model in the system."""

    class Tipo(models.IntegerChoices):
        CLIENTE = 1, "Cliente"
        TRABALHADOR = 2, "Trabalhador"
        ADM = 3, "Admin"

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="autores", null=True, blank=True)
    cpf = models.IntegerField(null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None,
    )
    capa = models.ForeignKey(Image, related_name="+", on_delete=models.PROTECT, null=True, blank=True, default=None)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    tipo = models.IntegerField(choices=Tipo.choices, default=3)
    publicacao = models.CharField(max_length=300, null=True, blank=True)
    publicacaoFoto = models.ForeignKey(
        Image, related_name="+", on_delete=models.PROTECT, null=True, blank=True, default=None
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        """Meta options for the model."""

        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
