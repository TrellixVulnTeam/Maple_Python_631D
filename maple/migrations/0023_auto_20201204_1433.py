# Generated by Django 2.2 on 2020-12-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0022_auto_20201204_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
