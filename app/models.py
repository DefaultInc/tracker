from django.db.models import (Model, TextField, DecimalField, ForeignKey,
                              PositiveIntegerField, SET_NULL, CASCADE)
from daas.models import User


class Category(Model):
    name = TextField()

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-id']
    def __str__(self):
        return self.name

class Transaction(Model):
    user = ForeignKey(User, related_name='transactions', null=True, blank=True, on_delete=CASCADE)
    name = TextField()
    price = DecimalField(decimal_places=4, max_digits=10)
    category = ForeignKey(Category, related_name='transactions', null=True, blank=True, on_delete=SET_NULL)
    date = PositiveIntegerField()

    def __str__(self):
        return self.name

class Course(Model):
    name = TextField()
    price = DecimalField(decimal_places=4, max_digits=10)

    def __str__(self):
        return self.price