# Generated by Django 4.0 on 2022-11-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]