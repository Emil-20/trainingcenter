# Generated by Django 4.0 on 2022-04-01 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingapp', '0006_remove_reported_issue_reported_issue_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_team',
            name='create_team_count',
        ),
    ]
