from django.db import models


class User(models.Model):

    # Fields
    username: models.CharField(max_length=50)
    password: models.CharField(max_length=50)

    cad: models.IntegerField()
    auCo: models.IntegerField()
