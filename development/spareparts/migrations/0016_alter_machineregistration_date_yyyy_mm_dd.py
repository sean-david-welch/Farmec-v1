# Generated by Django 4.1.2 on 2023-01-20 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts', '0015_rename_date_machineregistration_date_yyyy_mm_dd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machineregistration',
            name='date_YYYY_MM_DD',
            field=models.DateField(blank=True, null=True),
        ),
    ]
