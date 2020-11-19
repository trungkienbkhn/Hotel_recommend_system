# Generated by Django 3.1.1 on 2020-11-19 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_view_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('rank_score', models.FloatField(max_length=20, null=True)),
                ('root', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.root')),
            ],
        ),
    ]
