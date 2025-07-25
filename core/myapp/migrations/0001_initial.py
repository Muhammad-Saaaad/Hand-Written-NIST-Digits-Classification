# Generated by Django 5.2.4 on 2025-07-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image_Result",
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
                ("image", models.ImageField(upload_to="")),
                ("predicted_digit", models.IntegerField()),
                ("prediction_score", models.FloatField()),
            ],
        ),
    ]
