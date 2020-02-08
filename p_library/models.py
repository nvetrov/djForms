from django.db import models


class Friend(models.Model):
    name = models.TextField(verbose_name='Кому одолжил(Имя)')
    borrowed = models.DateField(verbose_name='Дата выдачи книги', null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)