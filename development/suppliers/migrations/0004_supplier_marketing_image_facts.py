# Generated by Django 4.1.2 on 2022-12-03 17:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_alter_supplier_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='marketing_image',
            field=models.ImageField(blank=True, default='models/default.jpg', null=True, upload_to='models/'),
        ),
        migrations.CreateModel(
            name='Facts',
            fields=[
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier')),
            ],
        ),
    ]