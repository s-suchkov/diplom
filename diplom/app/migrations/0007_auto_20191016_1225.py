# Generated by Django 2.1.1 on 2019-10-16 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_products_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='author',
            field=models.EmailField(max_length=254),
        ),
    ]
