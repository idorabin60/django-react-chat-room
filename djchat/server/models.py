from django.db import models
from django.conf import settings


def category_icon_upload_path(instance, filename):
    # If instance.pk exists (for editing an existing category) or instance is saved in the database
    if instance.pk:
        # Get the current pk value and use it in the upload path
        current_pk = instance.pk
    else:
        # If instance.pk is None, it means it's a new category and pk is not assigned yet
        # To get the next available pk, you can find the highest existing pk and add 1
        highest_pk = Category.objects.order_by("-pk").first()
        current_pk = highest_pk.pk + 1 if highest_pk else 1
    return f"category/{current_pk}/category_icon{filename}"


class Category(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    icon = models.FileField(upload_to=category_icon_upload_path, null=True, blank=True)

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
