# Generated by Django 2.2.4 on 2019-10-23 13:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estate_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Property',
            new_name='PropertyModel',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
