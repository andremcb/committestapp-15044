# Generated by Django 2.2.13 on 2020-06-16 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_homepage_tst3"),
    ]

    operations = [
        migrations.RemoveField(model_name="homepage", name="commit_2",),
        migrations.RemoveField(model_name="homepage", name="commit_3",),
        migrations.RemoveField(model_name="homepage", name="commit_4",),
        migrations.RemoveField(model_name="homepage", name="tst3",),
    ]
