# Generated by Django 4.2.1 on 2023-07-09 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_word_story_storyai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyai',
            name='story',
            field=models.TextField(blank=True, max_length=550, null=True),
        ),
    ]