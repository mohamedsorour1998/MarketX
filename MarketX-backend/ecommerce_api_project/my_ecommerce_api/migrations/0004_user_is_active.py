# Generated by Django 4.1.7 on 2023-05-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_ecommerce_api', '0003_remove_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
