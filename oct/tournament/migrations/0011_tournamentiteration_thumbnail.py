# Generated by Django 4.2.2 on 2023-06-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0010_tournamentround_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentiteration',
            name='thumbnail',
            field=models.CharField(default='oct3-thumbnail.png', max_length=32),
            preserve_default=False,
        ),
    ]
