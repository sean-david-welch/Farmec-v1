# Generated by Django 4.1.2 on 2023-01-30 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_special_link_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='special',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]