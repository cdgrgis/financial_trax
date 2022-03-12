from django.db import models
from django.contrib.auth import get_user_model

# v3

from .fund import Fund

class FundInfo(models.Model):
  amount_owned=models.FloatField()
  balance=models.DecimalField(max_digits=17, decimal_places=2)


  account = models.ForeignKey('Account', on_delete=models.CASCADE)

  fund = models.ForeignKey(Fund, on_delete=models.CASCADE)


  def __str__(self):
      return f"{self.id} - Owned: {self.amount_owned}, Balance: {self.balance}"


