# Generated by Django 3.0.2 on 2020-08-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_com', '0002_productdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='imagefile',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]
