# Generated by Django 4.1.2 on 2023-01-27 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_exhibition_delete_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exhibition',
            options={'ordering': ['created']},
        ),
    ]
