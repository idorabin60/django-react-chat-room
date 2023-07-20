from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(max_length=1000)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="server_owner"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="server_category"
    )
    description = models.CharField(max_length=250, null=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class Chanel(models.Model):
    name = models.CharField(max_length=1000)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic = models.CharField(max_length=250, null=True)
    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="chanel_server"
    )

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Chanel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# Create your models here.
