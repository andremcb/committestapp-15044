# Generated by Django 2.2.13 on 2020-06-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='commit_2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]