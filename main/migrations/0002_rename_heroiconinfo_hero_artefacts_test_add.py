# Generated by Django 4.2.3 on 2023-08-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HeroIconInfo',
            new_name='Hero',
        ),
        migrations.AddField(
            model_name='artefacts',
            name='test_add',
            field=models.TextField(default=1, verbose_name='test'),
            preserve_default=False,
        ),
    ]
