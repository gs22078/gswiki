# Generated by Django 5.0 on 2023-12-24 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_rename_slug_article_url_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revision',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
