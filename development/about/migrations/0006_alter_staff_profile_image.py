# Generated by Django 4.1.2 on 2022-12-03 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_alter_staff_social_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='profile_image',
            field=models.ImageField(blank=True, default='models/default.jpg', null=True, upload_to='models/'),
        ),
    ]
