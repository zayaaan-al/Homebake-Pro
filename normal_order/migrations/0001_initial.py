# Generated by Django 3.2.21 on 2024-01-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NormalOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=25)),
                ('amount', models.CharField(max_length=30)),
                ('wishes', models.CharField(max_length=40)),
                ('weight', models.CharField(max_length=30)),
                ('shape', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'normal_order',
                'managed': False,
            },
        ),
    ]
