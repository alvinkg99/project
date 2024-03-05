# Generated by Django 4.2.7 on 2023-12-14 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_delete_mycart'),
    ]

    operations = [
        migrations.CreateModel(
            name='mycart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('delivered', models.BooleanField(default=False)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productdet')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usignup')),
            ],
        ),
    ]