# Generated by Django 2.2.4 on 2020-01-04 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('estate_app', '0009_auto_20200103_1416'),
        ('accounts', '0004_auto_20200103_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
