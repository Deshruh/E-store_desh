# Generated by Django 4.2.11 on 2024-03-27 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]