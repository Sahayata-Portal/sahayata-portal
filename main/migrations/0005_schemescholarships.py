# Generated by Django 3.2.12 on 2022-03-31 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_mailform_employment'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchemeScholarships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('closing_date', models.DateTimeField()),
                ('guideline', models.URLField()),
                ('faq', models.URLField()),
            ],
        ),
    ]