# Generated by Django 4.0.3 on 2022-03-21 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films_gallery', '0003_alter_film_content_alter_film_date_publisher_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='is_published',
        ),
        migrations.AlterField(
            model_name='film',
            name='en_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название на английском'),
        ),
        migrations.AlterField(
            model_name='film',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='film',
            name='slang',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='film',
            name='time',
            field=models.IntegerField(blank=True, verbose_name='Длительность фильма'),
        ),
    ]
