# Generated by Django 4.1.2 on 2022-12-10 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0015_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='machine',
            options={'ordering': ['created']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['created']},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'ordering': ['created']},
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
