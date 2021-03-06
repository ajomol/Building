# Generated by Django 3.0 on 2022-04-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grp_name', models.CharField(max_length=40)),
                ('grp_description', models.TextField(max_length=400)),
                ('is_status', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
