# Generated by Django 4.1.2 on 2023-01-09 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_stat_svg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stat',
            name='svg',
        ),
        migrations.AlterField(
            model_name='stat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='models/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg'])]),
        ),
    ]