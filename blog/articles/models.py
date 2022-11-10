from django.db import models

class Author(models.Model):
    firstname = models.fields.CharField(max_length=50)
    lastname = models.fields.CharField(max_length=50)
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Article(models.Model): #notre classe hérite de models.Model qui est la classe de base de modèle de Django
    
    class Genre(models.TextChoices): #Genre est une classe imbrqué qui hérite de models.TextChoices qui est conçu pour définir une liste de choix
        SHONEN = "SH"
        SEININ ="SN"
    title = models.fields.CharField(max_length=20)
    description = models.fields.TextField()
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    author = models.ForeignKey(Author,null=True, on_delete=models.SET_NULL)

