from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=100)


class Donation(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
