# Generated by Django 3.1.2 on 2021-04-12 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('Qid', models.IntegerField()),
                ('Title', models.CharField(max_length=40)),
                ('Date', models.DateField()),
                ('Query', models.CharField(max_length=2000)),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.adduser')),
            ],
        ),
        migrations.CreateModel(
            name='Answer_query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qid', models.IntegerField()),
                ('Date', models.DateField()),
                ('Answer', models.CharField(max_length=2000)),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.adduser')),
            ],
        ),
    ]
