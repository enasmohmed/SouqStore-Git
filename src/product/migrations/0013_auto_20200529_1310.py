# Generated by Django 3.0.6 on 2020-05-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20200529_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDIsBestSeller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDIsNew',
            field=models.BooleanField(default=True),
        ),
    ]
