# Generated by Django 4.1 on 2022-08-14 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wukong_fitness', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='price',
            field=models.IntegerField(),
        ),
    ]
