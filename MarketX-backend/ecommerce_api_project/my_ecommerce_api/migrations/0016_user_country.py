# Generated by Django 4.1.7 on 2023-05-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_ecommerce_api', '0015_remove_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='United States', max_length=20),
        ),
    ]
