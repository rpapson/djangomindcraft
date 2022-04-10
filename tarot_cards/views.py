from django.shortcuts import render
from tarot_cards.models import TarotCard


# Create your views here.
def card_view(request):
    result = TarotCard.objects.order_by('?').first()
    choice = {'title':result.title,'src':result.src,'text':result.text}

    return render(request, 'tarot_cards/card.html', context = choice)
