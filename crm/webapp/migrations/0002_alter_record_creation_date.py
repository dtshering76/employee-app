# Generated by Django 5.0.6 on 2024-07-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='creation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
