# Generated by Django 3.2.8 on 2021-11-01 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servey',
            fields=[
                ('rnum', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(blank=True, max_length=4, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('co_survey', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'servey',
                'managed': False,
            },
        ),
    ]
