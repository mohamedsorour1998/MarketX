# Generated by Django 4.1.7 on 2023-05-06 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_ecommerce_api', '0010_alter_checkout_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_ecommerce_api.order'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_ecommerce_api.user'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_ecommerce_api.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_ecommerce_api.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='zip_code',
            field=models.CharField(max_length=20),
        ),
    ]
