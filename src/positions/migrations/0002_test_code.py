# Generated by Django 3.1.5 on 2021-01-13 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
