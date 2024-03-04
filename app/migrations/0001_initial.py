# Generated by Django 5.0.3 on 2024-03-04 19:38

import banjo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', banjo.models.StringField(default='')),
                ('answer', banjo.models.StringField(default='')),
                ('guesses', banjo.models.IntegerField(default=0)),
                ('correct', banjo.models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
