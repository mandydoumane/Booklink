# Generated by Django 3.1.7 on 2021-05-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210512_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oeuvre',
            name='artists',
        ),
        migrations.AddField(
            model_name='oeuvre',
            name='auteurs',
            field=models.ManyToManyField(blank=True, related_name='oeuvres', to='store.Artist'),
        ),
    ]
