# Generated by Django 2.2 on 2020-12-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0024_auto_20201204_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='images/none/sz.jpg', upload_to='images'),
        ),
    ]
