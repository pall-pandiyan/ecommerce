from django.contrib.auth import get_user_model
from django.db import models


class UserProfileModel(models.Model):
    """
    Custom user model with custom fields.
    Developer: Pall Pandiyan.S
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id"]
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
