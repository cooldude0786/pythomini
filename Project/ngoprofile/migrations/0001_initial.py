# Generated by Django 4.1.7 on 2023-04-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ngo_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngoname', models.CharField(max_length=255)),
                ('slogan', models.CharField(max_length=255)),
                ('vision', models.CharField(max_length=255)),
                ('founderstmt', models.CharField(max_length=255)),
                ('startdate', models.DateField()),
                ('operatonal', models.CharField(max_length=255)),
                ('fromstate', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('capacity', models.CharField(max_length=255)),
            ],
        ),
    ]
