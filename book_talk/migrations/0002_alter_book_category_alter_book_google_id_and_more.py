# Generated by Django 4.0.2 on 2022-02-16 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_talk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='google_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='preview_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
