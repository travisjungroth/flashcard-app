from flashcards.views import DeckListView


class HomePageView(DeckListView):
    template_name = 'home.html'
