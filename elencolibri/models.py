
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Bookshelf(models.Model):

    name = models.CharField(max_length=200)
    house = models.CharField(max_length=2, choices=[('AR', 'AR'), ('Pe', 'Pe')], default='AR')
    room = models.CharField(max_length=9,
                            choices=[('Cantina', 'basement'), ('Corridoio', 'hallway'), ('Salotto', 'living room'),
                                     ('Studio', 'study'), ('Camera', 'bedroom')])

    def __str__(self):
        return f"{self.house} - {self.room} {self.name}"

    class Meta:
        ordering = ['name']


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    volume = models.IntegerField(blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.PROTECT, blank=True, null=True)
    side = models.CharField(max_length=1, choices=[('l', 'left'), ('r', 'right')], blank=True, null=True)
    shelf = models.IntegerField(choices=list(enumerate(range(0, 9))), help_text='from bottom', blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True)
    vote = models.IntegerField(choices=[(5, 5), (6, 6), (7, 7)], blank=True, null=True)
    support = models.CharField(max_length=1,
                               choices=[('b', 'book'), ('d', 'digital'), ('c', 'copy'), ('n', 'notes')],
                               default='b', blank=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        name = f'{self.title}'
        if self.volume:
            name += f'Vol: {self.volume}'
        if self.author:
            name += f' - {self.author}'
        if self.topic:
            name += f', {self.topic}'
        if self.bookshelf:
            name += f', {self.bookshelf}'
        if self.comment:
            name += f', {self.comment}'
        return name

    class Meta:
        ordering = ['title']
