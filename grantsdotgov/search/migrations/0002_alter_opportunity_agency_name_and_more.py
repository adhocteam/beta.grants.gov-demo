# Generated by Django 4.1.7 on 2023-03-16 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='agency_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='close_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='post_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
