# Generated by Django 4.1.6 on 2023-02-11 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripepayments', '0003_delete_stripeproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentproduct',
            name='file',
        ),
        migrations.AddField(
            model_name='paymentproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='models/'),
        ),
    ]
