# Generated by Django 4.1.2 on 2022-12-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0007_mxfact_heading_sipfact_heading_sulkyfact_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='fact_heading',
            field=models.TextField(blank=True, null=True),
        ),
    ]