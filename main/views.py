from django.shortcuts import render
from .models import Hero, Artefacts, Weapon

def home(request):
    return render(request, 'main/home.html')

def wanderer(request):
    hero = Hero.objects.get(hero_name="Мандрівник")
    art_1 = Artefacts.objects.get(art_name="Хроніки Чертогів у пустелі")
    art_2 = Artefacts.objects.get(art_name="Спогади Сіменави")
    art_3 = Artefacts.objects.get(art_name="Смарагдова тінь")
    art_4 = Artefacts.objects.get(art_name="Золота трупа")
    return render(request, 'main/wanderer.html', {'hero' : hero,
                                                  'art_1' : art_1,
                                                  'art_2' : art_2,
                                                  'art_3' : art_3,
                                                  'art_4' : art_4})