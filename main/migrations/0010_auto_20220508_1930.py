# Generated by Django 3.2.12 on 2022-05-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20220508_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translations',
            old_name='en',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='translations',
            old_name='hi',
            new_name='tran',
        ),
        migrations.AddField(
            model_name='translations',
            name='lang',
            field=models.CharField(default='en', max_length=10),
            preserve_default=False,
        ),
    ]
