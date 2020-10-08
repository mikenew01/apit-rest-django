# Generated by Django 3.1.2 on 2020-10-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('active', models.BooleanField(default=True, max_length=1)),
            ],
            options={
                'db_table': 'client',
            },
        ),
    ]
