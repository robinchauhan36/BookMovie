from django.db import models
from accounts.models import ModelMixin
from accounts.models import notification_create
from django.contrib.auth.models import User


# Create your models here.
class StripeAccount(ModelMixin):
    account_id = models.CharField(max_length=500, default='')

    def save(self, *args, **kwargs):
        try:
            message = f'your Account is successfully connected with stripe.'
            notification_create(user=self.created_by, message=message)
        except Exception as e:
            print(f'Notification not create: {e}')
        return super(StripeAccount, self).save(*args, **kwargs)


class PaymentHistory(ModelMixin):
    TRANSACTION_TYPE = (
        ('DR', 'DEBIT'),
        ('CR', 'CREDIT')
    )
    amount = models.CharField(default='', max_length=2000)
    transaction_id = models.CharField(max_length=500, default='')
    type = models.CharField(choices=TRANSACTION_TYPE, default='DR', max_length=100)
