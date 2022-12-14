# Generated by Django 4.1.1 on 2022-09-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="decimalToPercentageCalculator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("inputEnter", models.CharField(max_length=250)),
                ("detailStep", models.TextField()),
                ("finalAnswer", models.CharField(max_length=300)),
                ("slug", models.CharField(max_length=300)),
                ("solutionTitle", models.CharField(max_length=250)),
                ("date_modified", models.DateTimeField()),
            ],
            options={"verbose_name_plural": "decimalToPercentageCalculator",},
        ),
        migrations.CreateModel(
            name="dividedByWhatCalculator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("inputEnter", models.CharField(max_length=250)),
                ("detailStep", models.TextField()),
                ("finalAnswer", models.CharField(max_length=300)),
                ("slug", models.CharField(max_length=300)),
                ("solutionTitle", models.CharField(max_length=250)),
                ("date_modified", models.DateTimeField()),
            ],
            options={"verbose_name_plural": "dividedByWhatCalculator",},
        ),
        migrations.CreateModel(
            name="moduloCalculator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("inputEnter", models.CharField(max_length=250)),
                ("detailStep", models.TextField()),
                ("finalAnswer", models.CharField(max_length=300)),
                ("slug", models.CharField(max_length=300)),
                ("solutionTitle", models.CharField(max_length=250)),
                ("date_modified", models.DateTimeField()),
            ],
            options={"verbose_name_plural": "moduloCalculator",},
        ),
        migrations.CreateModel(
            name="negativeDividedCalculator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("inputEnter", models.CharField(max_length=250)),
                ("detailStep", models.TextField()),
                ("finalAnswer", models.CharField(max_length=300)),
                ("slug", models.CharField(max_length=300)),
                ("solutionTitle", models.CharField(max_length=250)),
                ("date_modified", models.DateTimeField()),
            ],
            options={"verbose_name_plural": "negativeDividedCalculator",},
        ),
        migrations.CreateModel(
            name="percenttToDecimalCalculator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("inputEnter", models.CharField(max_length=250)),
                ("detailStep", models.TextField()),
                ("finalAnswer", models.CharField(max_length=300)),
                ("slug", models.CharField(max_length=300)),
                ("solutionTitle", models.CharField(max_length=250)),
                ("date_modified", models.DateTimeField()),
            ],
            options={"verbose_name_plural": "percenttToDecimalCalculator",},
        ),
    ]
