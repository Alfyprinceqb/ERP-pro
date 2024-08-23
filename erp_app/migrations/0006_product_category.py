# Generated by Django 4.2.1 on 2024-08-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_app', '0005_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.CharField(max_length=255, unique=True)),
                ('product_code', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.TextField(max_length=255)),
                ('product_category', models.CharField(max_length=255)),
                ('reorder_quantity', models.IntegerField()),
            ],
        ),
    ]