# Generated by Django 5.0.6 on 2024-06-12 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_tag_product_type_alter_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='tag',
            new_name='model_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.productcategory'),
            preserve_default=False,
        ),
    ]
