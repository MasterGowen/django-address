# Generated by Django 3.2.4 on 2021-06-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20200830_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='code',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
