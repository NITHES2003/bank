# Generated by Django 3.2.7 on 2021-09-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trasnsactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('debit', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('acbal', models.IntegerField()),
            ],
        ),
    ]
