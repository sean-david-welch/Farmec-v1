# Generated by Django 4.1.2 on 2023-01-13 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts', '0002_rename_sparepart_supplier_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PartPage',
            new_name='PartsPage',
        ),
        migrations.RenameModel(
            old_name='Supplier',
            new_name='SupplierPage',
        ),
    ]
