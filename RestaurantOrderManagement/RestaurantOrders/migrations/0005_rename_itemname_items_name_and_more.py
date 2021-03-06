# Generated by Django 4.0 on 2021-12-11 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantOrders', '0004_auto_20211209_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='ItemName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='Quantity',
            new_name='stock',
        ),
        migrations.RemoveField(
            model_name='items',
            name='OrderID',
        ),
        migrations.AddField(
            model_name='items',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='item_type',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
