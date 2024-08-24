# Generated by Django 4.2.1 on 2024-08-23 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=255, unique=True)),
                ('product_code', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.TextField(max_length=255)),
                ('reorder_quantity', models.IntegerField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='erp_app.vendor')),
            ],
        ),
    ]