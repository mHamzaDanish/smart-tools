# Generated by Django 3.2 on 2022-10-15 06:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('grammar', '0006_alter_recording_audio_recording'),
    ]

    operations = [
        migrations.AddField(
            model_name='recording',
            name='user_id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
