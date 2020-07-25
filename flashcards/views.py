from django.http import request
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from .models import Deck, Card


class DeckListView(ListView):
    model = Deck
    template_name = 'deck_list.html'
    context_object_name = 'all_deck_list'

    def get_object(self, **kwargs):
        deck = Deck.objects.get(id=self.kwargs['deckid'])
        return deck


class DeckUpdateView(UpdateView):
    model = Deck
    fields = ('name',)
    template_name = 'deck_update.html'
    context_object_name = 'deck_update'

    def get_object(self, **kwargs):
        deck = Deck.objects.get(id=self.kwargs['deckid'])
        return deck


class DeckCreateView(CreateView):
    model = Deck
    fields = ('name',)
    template_name = 'deck_create.html'


class DeckDeleteView(DeleteView):
    model = Deck
    template_name = 'deck_delete.html'
    success_url = reverse_lazy('deck_list')

    def get_object(self, **kwargs):
        deck = Deck.objects.get(id=self.kwargs['deckid'])
        return deck


class CardListView(ListView):
    model = Card
    template_name = 'card_list.html'
    context_object_name = 'card_list'

    def get_queryset(self):
        return super(CardListView, self).get_queryset().filter(deck=self.kwargs['deckid'])


class CardCreateView(CreateView):
    model = Card
    fields = ('deck', 'front', 'back',)
    template_name = 'card_create.html'


class CardUpdateView(UpdateView):
    model = Card
    fields = ('deck', 'front', 'back',)
    template_name = 'card_update.html'


class CardDeleteView(DeleteView):
    model = Card
    template_name = 'card_delete.html'
    success_url = reverse_lazy('card_list')


class FlashcardFrontView(DetailView):
    model = Card
    template_name = 'flashcard_front.html'
    next_id = Card.objects.order_by('-id').first().id + 1

    def get_queryset(self):
        return super(FlashcardFrontView, self).get_queryset().filter(deck=self.kwargs['deckid'])


class FlashcardBackView(DetailView):
    model = Card
    template_name = 'flashcard_back.html'
    next_id = Card.objects.order_by('-id').first().id + 1

    def get_queryset(self):
        return super(FlashcardBackView, self).get_queryset().filter(deck=self.kwargs['deckid'])
