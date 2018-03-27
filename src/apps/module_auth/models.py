from django.db import models

# Create your models here.

# Authentication backends
"""   Class ModelBackend    """
"""
    - Default authentication backend used by django
    - Aunthenticates using credentials like user identifier and Password
    - For Custom user models it is the field specified by USERNAME_FIELD

"""

from django.contrib.auth.models import AbstractBaseUser


class Example1(AbstractBaseUser):
    identifier = models.CharField("Identifier", max_length=400)
    USERNAME_FIELD = 'identifier'

    def __str__(self):
        return u'%s' % self.identifier