from django.contrib import admin
from .models import Hero, Artefacts, Weapon

models = (Hero, Artefacts, Weapon)

for model in models:
    admin.site.register(model)