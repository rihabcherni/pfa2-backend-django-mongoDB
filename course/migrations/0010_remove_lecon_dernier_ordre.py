# Generated by Django 4.1.13 on 2024-03-26 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_lecon_dernier_ordre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecon',
            name='dernier_ordre',
        ),
    ]
