# Generated by Django 2.2.13 on 2020-06-16 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_homepage_commit_5"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="commit_6",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]