# Generated by Django 5.1.4 on 2025-01-23 00:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movies_video_movies_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'ordering': ['-created_at'], 'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
        migrations.AddField(
            model_name='movies',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
