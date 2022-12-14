# Generated by Django 4.0.4 on 2022-11-16 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Numbers', '0047_horizontaltangent'),
    ]

    operations = [
        migrations.CreateModel(
            name='equationofarithmeticsequenceCalculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputEnter', models.CharField(max_length=250)),
                ('detailStep', models.TextField()),
                ('finalAnswer', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
                ('solutionTitle', models.CharField(max_length=250)),
                ('eq1', models.CharField(max_length=300)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'equationofarithmeticsequenceCalculator',
            },
        ),
    ]
