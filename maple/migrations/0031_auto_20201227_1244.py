# Generated by Django 2.2 on 2020-12-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0030_auto_20201205_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beef',
            name='large',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='beef',
            name='regular',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chicken',
            name='large',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chicken',
            name='regular',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='large',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='regular',
            field=models.FloatField(),
        ),
    ]
