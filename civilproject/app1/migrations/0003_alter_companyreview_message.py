# Generated by Django 4.1.5 on 2023-03-24 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_reviews_companyreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyreview',
            name='message',
            field=models.TextField(),
        ),
    ]
