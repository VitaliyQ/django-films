# Generated by Django 4.0.3 on 2022-03-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films_gallery', '0008_alter_producer_date_of_birth_alter_producer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]