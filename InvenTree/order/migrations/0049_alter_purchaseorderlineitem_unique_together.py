# Generated by Django 3.2.4 on 2021-08-12 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0040_alter_company_currency'),
        ('order', '0048_auto_20210702_2321'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='purchaseorderlineitem',
            unique_together={('order', 'part', 'quantity', 'purchase_price')},
        ),
    ]
