# Generated by Django 5.1.2 on 2024-10-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarcamaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
