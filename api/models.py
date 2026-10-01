from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.title

class Books(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="image/books/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    genge = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name