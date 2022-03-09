from django.db import models
from django.contrib.auth import get_user_model

class Fund(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.2/ref/models/fields/
  ticker_symbol=models.CharField(max_length=5)
  company_name=models.CharField(max_length=100)
  price=models.FloatField()


  owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.ticker_symbol} {self.company_name} is currently selling at {self.price}"

  def as_dict(self):
    """Returns dictionary version of Account models"""
    return {
        'id': self.id,
        'ticker_symbol': self.ticker_symbol,
        'company_name': self.company_name,
        'price': self.price
    }
