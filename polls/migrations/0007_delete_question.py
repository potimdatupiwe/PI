# Generated by Django 5.0.6 on 2024-07-01 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_question_graf_question_post_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
