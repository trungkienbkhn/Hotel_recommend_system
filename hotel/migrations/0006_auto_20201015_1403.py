# Generated by Django 3.1.1 on 2020-10-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_auto_20201015_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roothotel',
            name='description',
            field=models.CharField(max_length=4000, null=True),
        ),
    ]
