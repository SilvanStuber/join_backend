# Generated by Django 5.1.2 on 2024-11-05 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0009_alter_task_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercontact',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]