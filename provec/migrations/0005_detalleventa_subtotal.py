# Generated by Django 5.1.6 on 2025-03-05 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provec', '0004_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
