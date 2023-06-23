from django.db import models
from django.utils.translation import gettext as _


class StatusChoice(models.TextChoices):
    """

    """
    ACTIVE = 'A', _('active')
    INACTIVE = 'I', _('inactive')
