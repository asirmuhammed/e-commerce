# Generated by Django 4.2b1 on 2023-10-20 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='category_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]