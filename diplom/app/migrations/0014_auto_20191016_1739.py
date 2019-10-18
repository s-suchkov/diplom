# Generated by Django 2.1.1 on 2019-10-16 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20191016_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='article',
        ),
        migrations.AddField(
            model_name='products',
            name='article',
            field=models.ManyToManyField(to='app.Article'),
        ),
        migrations.RemoveField(
            model_name='products',
            name='basket',
        ),
        migrations.AddField(
            model_name='products',
            name='basket',
            field=models.ManyToManyField(to='app.Basket'),
        ),
    ]