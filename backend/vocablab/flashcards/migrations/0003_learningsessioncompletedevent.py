# Generated by Django 5.0.4 on 2024-04-16 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_learningsession'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningSessionCompletedEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('learning_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcards.learningsession')),
            ],
        ),
    ]
