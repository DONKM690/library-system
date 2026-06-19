from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20 ,unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()

    def __str__(self):
        return self.title