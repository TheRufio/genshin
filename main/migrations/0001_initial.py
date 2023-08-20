# Generated by Django 4.2.3 on 2023-08-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artefacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_name', models.CharField(max_length=100, verbose_name='Назва артефакта')),
                ('art_img', models.ImageField(upload_to='atrefacts', verbose_name='Картинка артефакта')),
                ('art_info', models.TextField(verbose_name='Інформація артефакта')),
            ],
        ),
        migrations.CreateModel(
            name='HeroIconInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_name', models.CharField(max_length=40, verbose_name="Ім'я героя")),
                ('hero_img', models.ImageField(upload_to='character', verbose_name='Картинка героя')),
                ('hero_element', models.CharField(max_length=40, verbose_name='Стихія героя')),
                ('hero_info', models.TextField(verbose_name='Інформація героя')),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon_name', models.CharField(max_length=100, verbose_name='Назва зброї')),
                ('weapon_img', models.ImageField(upload_to='', verbose_name='Картинка зброї')),
                ('weapon_info', models.TextField(verbose_name='Інформація картинки')),
            ],
        ),
    ]
