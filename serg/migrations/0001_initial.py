# Generated by Django 5.1.7 on 2025-03-12 15:56

import serg.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('posted', models.DateTimeField(auto_created=True)),
                ('postid', models.CharField(default=serg.models.GenID, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('author', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField(max_length=1048)),
            ],
        ),
    ]
