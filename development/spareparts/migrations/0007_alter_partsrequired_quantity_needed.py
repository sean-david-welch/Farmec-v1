# Generated by Django 4.1.2 on 2023-01-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts', '0006_alter_partsrequired_part_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partsrequired',
            name='quantity_needed',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
