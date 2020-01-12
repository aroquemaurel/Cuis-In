# Generated by Django 2.2.8 on 2020-01-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='city',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout"),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='note',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='postalcode',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='website',
            field=models.CharField(default='', max_length=128),
        ),
    ]