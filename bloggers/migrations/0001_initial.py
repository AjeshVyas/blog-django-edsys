# Generated by Django 3.0.5 on 2020-05-15 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=5000)),
                ('img', models.ImageField(upload_to='')),
                ('author', models.CharField(max_length=50)),
                ('upload_datetime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
