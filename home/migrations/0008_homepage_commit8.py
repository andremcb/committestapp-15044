# Generated by Django 2.2.13 on 2020-06-16 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_homepage_commit_6"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="commit8",
            field=models.DecimalField(
                blank=True, decimal_places=10, max_digits=30, null=True
            ),
        ),
    ]