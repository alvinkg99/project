# Generated by Django 4.2.7 on 2023-11-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_productdet'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('productid', models.CharField(max_length=50)),
            ],
        ),
    ]
