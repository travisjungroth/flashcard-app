from django.urls import path
from .views import *


urlpatterns = [
    path('', DeckListView.as_view(), name='deck_list'),
    path('new/', DeckCreateView.as_view(), name='deck_create'),
    path('<int:deckid>/', DeckUpdateView.as_view(), name='deck_update'),
    path('<int:deckid>/delete/', DeckDeleteView.as_view(), name='deck_delete'),
    path('<int:deckid>/start/<int:pk>/front/', FlashcardFrontView.as_view(), name='flashcard_front'),
    path('<int:deckid>/start/<int:pk>/back/', FlashcardBackView.as_view(), name='flashcard_back'),

    path('<int:deckid>/cards/', CardListView.as_view(), name='card_list'),
    path('cards/new/', CardCreateView.as_view(), name='card_create'),
    path('cards/<int:pk>/', CardUpdateView.as_view(), name='card_update'),
    path('cards/<int:pk>/delete/', CardDeleteView.as_view(), name='card_delete'),
]