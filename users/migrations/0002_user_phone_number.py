# Generated by Django 4.2.11 on 2024-03-25 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]