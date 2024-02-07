from django.db.models import (
    Model, CharField, ForeignKey, DO_NOTHING,
    IntegerField, DateField, DateTimeField
)


class Genre(Model):
    name = CharField(max_length=128, default='unknown')


class Game(Model):
    name = CharField(max_length=100)
    description = CharField(max_length=300)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING, null=True)
    rating = IntegerField(default=-1)
    release_date = DateField(default='1970-01-01')
    created = DateTimeField(auto_now_add=True)
