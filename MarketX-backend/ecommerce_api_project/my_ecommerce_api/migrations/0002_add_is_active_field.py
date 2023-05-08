from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_ecommerce_api', '0017_alter_user_country'
         ),  # Replace this with the latest migration in your app
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]