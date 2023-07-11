# Generated by Django 4.2.1 on 2023-07-09 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_remove_word_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='story',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='StoryAi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.TextField(blank=True, max_length=350, null=True)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words.word')),
            ],
        ),
    ]
