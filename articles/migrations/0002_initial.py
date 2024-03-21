# Generated by Django 4.2.11 on 2024-03-21 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articlecategory'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articletag'),
        ),
    ]
