# Generated by Django 3.2.5 on 2021-10-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20210104_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(allow_unicode=True),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
