# Generated by Django 4.0.2 on 2022-02-04 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheme',
            old_name='elgibility',
            new_name='eligibility',
        ),
    ]
