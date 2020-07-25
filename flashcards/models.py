from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Card(models.Model):
    deck = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        related_name='cards'
    )
    front = models.TextField()
    back = models.TextField()

    def __str__(self):
        return self.front[:30]