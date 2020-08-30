from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Institution(models.Model):
    ORGANIZATIONS = [
        (0, "Fundacja"),
        (1, "Organizacja pozarządowa"),
        (2, "Zbiórka lokalna")
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(verbose_name="Opis instytucji")
    type = models.PositiveIntegerField(choices=ORGANIZATIONS, default=0)
    categories = models.ManyToManyField(Category, related_name="category_institution")

    def __str__(self):
        return f"{self.name}"

class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category, related_name="category_donation")
    institution = models.ForeignKey(Institution, related_name="institution_donation", on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number =models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(null=True)
    user = models.ForeignKey(User, related_name="user_donation", on_delete=models.CASCADE)
