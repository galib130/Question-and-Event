# Generated by Django 3.2.5 on 2021-10-31 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0011_alter_group_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
