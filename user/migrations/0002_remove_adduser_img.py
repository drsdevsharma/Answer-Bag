# Generated by Django 3.1.2 on 2021-04-13 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adduser',
            name='img',
        ),
    ]