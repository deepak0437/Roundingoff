# Generated by Django 4.0.4 on 2022-11-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Numbers', '0035_numberminuspercentcalculator_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='atsequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('func', models.CharField(max_length=256)),
                ('solution', models.CharField(max_length=256)),
            ],
        ),
    ]