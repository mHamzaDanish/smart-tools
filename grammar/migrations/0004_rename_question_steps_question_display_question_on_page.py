# Generated by Django 3.2 on 2022-10-09 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grammar', '0003_auto_20221009_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_steps',
            new_name='display_question_on_page',
        ),
    ]