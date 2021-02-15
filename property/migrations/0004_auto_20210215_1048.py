# Generated by Django 2.2.4 on 2021-02-15 07:48

from django.db import migrations


def add_value_new_building(apps, shema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = False
        if flat.construction_year >= 2015:
            flat.new_building = True
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(add_value_new_building)
    ]