from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Account(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.2/ref/models/fields/
  name = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  balance = models.FloatField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The account named {self.name} held by {self.company} has a balance of {self.balance}"

  def as_dict(self):
    """Returns dictionary version of Account models"""
    return {
        'id': self.id,
        'name': self.name,
        'company': self.company,
        'balance': self.balance
    }
