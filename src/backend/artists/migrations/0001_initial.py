# Generated by Django 5.1.5 on 2025-02-26 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbid', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('bio', models.TextField(blank=True)),
                ('avatar', models.ImageField(default='avatars/default.jpg', upload_to='avatars/')),
                ('added_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
