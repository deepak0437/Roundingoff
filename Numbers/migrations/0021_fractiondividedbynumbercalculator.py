# Generated by Django 4.0.4 on 2022-10-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Numbers', '0020_sequentialpercentagecalculator'),
    ]

    operations = [
        migrations.CreateModel(
            name='fractiondividedbynumberCalculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputEnter', models.CharField(max_length=250)),
                ('detailStep', models.TextField()),
                ('finalAnswer', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
                ('solutionTitle', models.CharField(max_length=250)),
                ('date_modified', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'fractiondividedbynumberCalculator',
            },
        ),
    ]
