# Generated by Django 4.0.2 on 2022-02-09 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_dog_owner_remove_allergy_drink_allergy_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dog',
            table='dogs',
        ),
    ]
