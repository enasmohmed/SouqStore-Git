# Generated by Django 3.0.6 on 2020-05-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_prcslug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='PRCSlug',
        ),
        migrations.AddField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
    ]