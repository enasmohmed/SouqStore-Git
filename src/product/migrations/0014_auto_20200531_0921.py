# Generated by Django 3.0.6 on 2020-05-31 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
        ('product', '0013_auto_20200529_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='PRDIsBestSeller',
        ),
        migrations.RemoveField(
            model_name='product',
            name='PRDIsNew',
        ),
        migrations.AddField(
            model_name='product',
            name='PRDISBestSeller',
            field=models.BooleanField(default=False, verbose_name='Best Seller'),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDISNew',
            field=models.BooleanField(default=True, verbose_name='New Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.Brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDDesc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(blank=True, null=True, verbose_name='Product URL'),
        ),
    ]
