# Generated by Django 3.2.9 on 2021-11-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeans', '0002_alter_datajeans_stok'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datajeans',
            name='harga',
            field=models.IntegerField(max_length=100),
        ),
    ]
