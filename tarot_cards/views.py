from django.shortcuts import render
from tarot_cards.models import TarotCard


# Create your views here.
def card_view(request):
    result = TarotCard.objects.order_by('?').first()
    choice = {'title':result.title,'src':result.src,'text':result.text}

    return render(request, 'tarot_cards/card.html', context = choice)

def card_accordian_view(request):
    result = TarotCard.objects.order_by('?').first()
    choice = {'title':result.title,'src':result.src,'text':result.text}

    return render(request, 'tarot_cards/card_accordian.html', context = choice)

def list_cards_view(request):
    result = TarotCard.objects.all()
    context = {'cards':result}
    return render(request, 'tarot_cards/list_cards.html', context = context)