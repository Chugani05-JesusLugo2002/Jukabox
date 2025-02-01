# Generated by Django 5.1.5 on 2025-02-01 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('songs', '0002_alter_song_added_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.ManyToManyField(related_name='songs', to='genres.genre'),
        ),
    ]
