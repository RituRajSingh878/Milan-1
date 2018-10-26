# Generated by Django 2.0.6 on 2018-10-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Found',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.FileField(upload_to='')),
                ('location', models.CharField(max_length=500)),
                ('condition', models.CharField(max_length=500)),
                ('provider_name', models.CharField(max_length=500)),
                ('provider_email', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Lost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.FileField(upload_to='')),
                ('person_name', models.CharField(max_length=500)),
                ('provider_email', models.EmailField(max_length=500)),
                ('provider_name', models.CharField(max_length=500)),
            ],
        ),
    ]