# Generated by Django 5.0 on 2024-01-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denumire', models.CharField(max_length=255)),
                ('firma_producatoare', models.CharField(max_length=255)),
                ('descriere', models.TextField()),
                ('cumparat', models.BooleanField(default=False)),
                ('imagine', models.ImageField(upload_to='SmartShopping/static/')),
            ],
        ),
    ]