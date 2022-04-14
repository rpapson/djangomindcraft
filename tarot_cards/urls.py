from django.urls import path
from . import views

app_name = 'tarot_cards'

urlpatterns = [
    path('',views.card_view),
    path('list_cards/',views.list_cards_view),
    path('accordian_cards/',views.card_accordian_view)
    ]