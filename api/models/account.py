from django.db import models
from django.contrib.auth import get_user_model

from .fund_info import FundInfo


# Create your models here.
class Account(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.2/ref/models/fields/
  type = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  inception = models.DateField()
  account_number = models.CharField(max_length=100)

  funds = models.ManyToManyField(
    'Fund',
    through=FundInfo,
    through_fields=('account', 'fund'),
    related_name='fund_infos',
    blank=True
  )

  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"Id:{self.id} | The {self.type} account {self.account_number} held by {self.company} has a balance of {self.balance}"

  def as_dict(self):
    """Returns dictionary version of Account models"""
    return {
        'id': self.id,
        'type': self.type,
        'company': self.company,
        'balance': self.balance,
        'inception': self.inception,
        'account_number': self.account_number,

    }
