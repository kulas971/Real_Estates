# Generated by Django 2.2.4 on 2019-10-22 20:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    atomic = False
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=10000)),
                ('price', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=64)),
                ('estate_type', models.CharField(choices=[(1, 'Flat'), (2, 'House'), (3, 'Plot')], default='Flat', max_length=12)),
                ('author', models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('property', models.ForeignKey(on_delete='cascade', related_name='images', to='estate_app.Property')),
            ],
        ),
    ]
