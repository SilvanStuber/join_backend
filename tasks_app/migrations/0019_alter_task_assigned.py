# Generated by Django 5.1.2 on 2024-11-24 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0018_remove_task_owner_task_creator_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
