# Generated by Django 3.1.1 on 2020-09-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_com', '0007_auto_20200911_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyproductdetail',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='companyproductdetail',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
