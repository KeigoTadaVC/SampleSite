from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import WeddingCard


def index(request):
    return render(request, 'promotion/index.html')

def showcard(request, card_id):
    card = get_object_or_404(WeddingCard, pk=card_id)
    return render(request, 'promotion/showcard.html', {'card':card})
