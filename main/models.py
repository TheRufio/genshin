from django.db import models

class Hero(models.Model):
    hero_name = models.CharField("Ім'я героя", max_length=40)
    hero_img = models.ImageField('Картинка героя', upload_to='character')
    hero_element = models.CharField('Стихія героя', max_length=40)
    hero_info = models.TextField('Інформація героя')

    def __str__(self):
        return self.hero_name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажі'

class Artefacts(models.Model):
    art_name = models.CharField("Назва артефакта", max_length=100)
    art_img = models.ImageField("Картинка артефакта", upload_to='atrefacts')
    
    def __str__(self):
        return self.art_name

    class Meta:
        verbose_name = 'Артефакт'
        verbose_name_plural = 'Артефакти'

class Weapon(models.Model):
    weapon_name = models.CharField('Назва зброї', max_length=100)
    weapon_img = models.ImageField('Картинка зброї')
    weapon_info = models.TextField('Інформація картинки')

    def __str__(self):
        return self.weapon_name

    class Meta:
        verbose_name = 'Зброя'
        verbose_name_plural = 'Зброя'