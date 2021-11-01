# Generated by Django 3.2.5 on 2021-10-31 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_alter_group_slug'),
        ('posts', '0033_auto_20211029_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(limit_choices_to={'name__in': 'objects'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='groups.group'),
        ),
    ]
