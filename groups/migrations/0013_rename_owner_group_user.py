# Generated by Django 3.2.5 on 2021-10-31 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0012_alter_group_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='owner',
            new_name='user',
        ),
    ]
