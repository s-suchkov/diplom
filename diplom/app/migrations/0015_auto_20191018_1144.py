# Generated by Django 2.1.1 on 2019-10-18 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20191016_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='basket',
        ),
        migrations.AddField(
            model_name='basket',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, related_name='bas', to='app.Products'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ord', to='app.Order'),
        ),
        migrations.AlterField(
            model_name='products',
            name='article',
            field=models.ManyToManyField(blank=True, null=True, to='app.Article'),
        ),
    ]
