# Generated by Django 5.1.5 on 2025-01-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('songs', models.ManyToManyField(blank=True, to='songs.song')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
