# Generated by Django 5.0.6 on 2024-06-20 04:15

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                ("name", models.CharField(max_length=255)),
                ("specialty", models.CharField(max_length=255)),
                ("contact", models.CharField(default="N/A", max_length=255)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
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
                ("name", models.CharField(max_length=255)),
                ("dob", models.DateField(default=datetime.date.today)),
                ("gender", models.CharField(max_length=10)),
                ("contact", models.CharField(default="N/A", max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="MedicalHistory",
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
                ("description", models.TextField()),
                ("date", models.DateField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.patient"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Appointment",
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
                ("date", models.DateTimeField()),
                (
                    "reason",
                    models.CharField(default="General Consultation", max_length=255),
                ),
                ("notes", models.TextField(default="No notes")),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.doctor"
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.patient"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateField()),
                ("status", models.CharField(max_length=255)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.patient"
                    ),
                ),
            ],
        ),
    ]
