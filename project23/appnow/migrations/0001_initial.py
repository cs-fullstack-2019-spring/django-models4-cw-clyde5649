# Generated by Django 2.0.6 on 2019-02-21 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mom_first_name', models.CharField(max_length=30)),
                ('mom_last_name', models.IntegerField(max_length=10)),
                ('mom_phone_number', models.DateField(max_length=10)),
            ],
        ),
    ]
