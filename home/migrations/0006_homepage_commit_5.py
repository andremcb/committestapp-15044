# Generated by Django 2.2.13 on 2020-06-16 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_homepage_commit_4"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="commit_5",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
