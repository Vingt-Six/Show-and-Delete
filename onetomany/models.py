from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=30)
    def __str__(self):
        return self.genre

class Gens(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    sofia = models.ForeignKey(Genre, on_delete=models.CASCADE)