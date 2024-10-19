# Generated by Django 5.1.2 on 2024-10-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=180)),
                ('author', models.CharField(max_length=100)),
                ('read', models.BooleanField(default=True)),
            ],
        ),
    ]
