from datetime import datetime, timezone

from django.db import models
from base import Base


class User(Base):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True, db_index=True
    )
    userTypes = ModelChoices.getChoices('userTypes')
    user_role_types = ModelChoices.getChoices('user_role_types')
    is_active = models.BooleanField(default=1)
    mobile = models.CharField(
        max_length=20, null=True, blank=True, unique=True
    )
    countryCode = models.CharField(max_length=10, default="+91")
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    updated = models.DateTimeField(auto_now=True, db_index=True, null=True)
    isRM = models.PositiveSmallIntegerField(default=0)
    firstLogin = models.PositiveSmallIntegerField(default=1)
    isDirect = models.PositiveSmallIntegerField(default=0)
    isTaxReportGenerated = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(
        max_length=20, choices=userTypes, default=TYPE_IND, blank=True, null=True
    )
    isInternational = models.PositiveSmallIntegerField(default=0)
    device_tokens = JSONField(null=True)
    credit_report_data = JSONField(null=True)
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []
    wa_consent = models.CharField(max_length=25, default=None, null=True)
    paid = models.PositiveSmallIntegerField(blank=True, default=0)
    role_type = models.PositiveSmallIntegerField(choices=user_role_types, default=0)
    role_type_mark = models.PositiveSmallIntegerField(
        choices=role_type_mark_choices, default=0
    )
    user_type_mark = models.PositiveSmallIntegerField(
        choices=user_type_mark_choices, default=0
    )
    meta = JSONField(default=dict)
    android_ver = models.CharField(max_length=10, null=True, blank=True, db_index=True)
    ios_ver = models.CharField(max_length=10, null=True, blank=True, db_index=True)
    is_subscribed = models.PositiveSmallIntegerField(default=0)
    subscription_plan = models.CharField(max_length=30, null=True, blank=True)
    boVerified = models.PositiveSmallIntegerField(default=0)
    panNum = models.CharField(max_length=10, validators=[
        MinLengthValidator(10)], blank=True, db_index=True)
    alt_countryCode = models.CharField(max_length=10, default="+91")
    alt_email = models.EmailField(null=True, blank=True, max_length=255)
    alt_mobile = models.CharField(max_length=20, null=True, blank=True)
    client_type = models.PositiveSmallIntegerField(
        

