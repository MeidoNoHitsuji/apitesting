# Generated by Django 3.0.5 on 2020-05-07 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('api', models.CharField(max_length=20)),
                ('dateofcreation', models.BigIntegerField(default=0)),
                ('description', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]