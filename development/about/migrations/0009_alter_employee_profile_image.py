# Generated by Django 4.1.2 on 2022-12-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_timeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='models/'),
        ),
    ]
