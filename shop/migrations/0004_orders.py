# Generated by Django 4.0.6 on 2022-09-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_jason', models.CharField(max_length=500)),
            ],
        ),
    ]
