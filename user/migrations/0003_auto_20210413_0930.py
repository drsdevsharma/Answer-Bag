# Generated by Django 3.1.2 on 2021-04-13 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_adduser_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adduser',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='adduser',
            old_name='password',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='adduser',
            old_name='ph_no',
            new_name='Ph_no',
        ),
    ]
