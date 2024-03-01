# Generated by Django 4.1.2 on 2023-01-13 19:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MachineRegistration',
            fields=[
                ('dealer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('dealer_address', models.CharField(blank=True, max_length=200, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=200, null=True)),
                ('owner_address', models.CharField(blank=True, max_length=200, null=True)),
                ('machine_model', models.CharField(blank=True, max_length=200, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=200, null=True)),
                ('install_date', models.CharField(blank=True, max_length=200, null=True)),
                ('invoice_number', models.CharField(blank=True, max_length=200, null=True)),
                ('complete_supply', models.BooleanField(default=False)),
                ('pdi_complete', models.BooleanField(default=False)),
                ('pto_correct', models.BooleanField(default=False)),
                ('machine_test_run', models.BooleanField(default=False)),
                ('safety_induction', models.BooleanField(default=False)),
                ('operator_handbook', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='SparePart',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('logo_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='models/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='WarrantyClaim',
            fields=[
                ('dealer', models.CharField(blank=True, max_length=200, null=True, verbose_name='Dealer')),
                ('dealer_contact', models.CharField(blank=True, max_length=200, null=True, verbose_name='Dealer Contact')),
                ('owner_name', models.CharField(blank=True, max_length=200, null=True)),
                ('machine_model', models.CharField(blank=True, max_length=200, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=200, null=True)),
                ('install_date', models.CharField(blank=True, max_length=200, null=True)),
                ('failure_date', models.CharField(blank=True, max_length=200, null=True)),
                ('repair_date', models.CharField(blank=True, max_length=200, null=True)),
                ('failure_details', models.TextField(blank=True, null=True)),
                ('repair_details', models.TextField(blank=True, null=True)),
                ('labour_hours', models.IntegerField(blank=True, null=True)),
                ('part_number', models.IntegerField(blank=True, null=True)),
                ('quantity_needed', models.IntegerField(blank=True, null=True)),
                ('invoice_number', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='PartPage',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('catalogue_link', models.URLField(blank=True, null=True, verbose_name='Catalogue Link')),
                ('supplier_page', models.URLField(blank=True, null=True, verbose_name='Supplier Page')),
                ('marketing_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='models/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spareparts.sparepart')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]