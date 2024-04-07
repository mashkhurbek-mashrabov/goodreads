from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from common.models import BaseModelV2


class Author(BaseModelV2):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(BaseModelV2):
    title = models.CharField(max_length=15)
    description = models.TextField()
    authors = models.ManyToManyField(Author, related_name="books")
    isbn = models.CharField(max_length=17)

    def __str__(self):
        return self.title


class BookReview(BaseModelV2):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    comment = models.CharField(max_length=256)
    stars = models.SmallIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])

    def __str__(self):
        return f"{self.book} | {self.user}"

