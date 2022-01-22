# Generated by Django 2.2 on 2022-01-20 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20220119_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(blank=True, max_length=70, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(blank=True, max_length=1000, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=70, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=models.CharField(blank=True, max_length=30, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(blank=True, max_length=400, verbose_name=''),
        ),
    ]