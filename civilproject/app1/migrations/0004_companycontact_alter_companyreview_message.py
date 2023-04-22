# Generated by Django 4.1.5 on 2023-03-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_companyreview_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('emails', models.CharField(max_length=50)),
                ('messages', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='companyreview',
            name='message',
            field=models.CharField(max_length=500),
        ),
    ]
