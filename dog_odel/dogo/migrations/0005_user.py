# Generated by Django 2.0.2 on 2018-03-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogo', '0004_auto_20180308_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=500)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('sexe', models.CharField(max_length=1)),
                ('date_naissance', models.DateField()),
            ],
        ),
    ]
