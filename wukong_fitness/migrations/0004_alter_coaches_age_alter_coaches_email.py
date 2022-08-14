# Generated by Django 4.1 on 2022-08-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wukong_fitness', '0003_coaches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coaches',
            name='Age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coaches',
            name='Email',
            field=models.EmailField(blank=True, default=' ', max_length=200),
        ),
    ]
