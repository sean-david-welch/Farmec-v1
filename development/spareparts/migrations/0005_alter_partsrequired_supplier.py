# Generated by Django 4.1.2 on 2023-01-14 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts', '0004_remove_warrantyclaim_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partsrequired',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spareparts.warrantyclaim'),
        ),
    ]