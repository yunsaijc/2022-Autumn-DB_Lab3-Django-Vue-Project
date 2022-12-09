# Generated by Django 3.2.16 on 2022-11-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_no', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('pwd', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'api',
                'managed': False,
            },
        ),
    ]
