# Generated by Django 4.1.7 on 2023-03-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_opportunity_addl_info_text_opportunity_addl_info_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='grant_id',
            field=models.CharField(blank=True, db_index=True, max_length=20, null=True),
        ),
    ]
