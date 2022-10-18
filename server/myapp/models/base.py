from datetime import datetime
from django.db import models


class Base(models.Models):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)