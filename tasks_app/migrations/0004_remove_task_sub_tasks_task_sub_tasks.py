# Generated by Django 5.1.2 on 2024-11-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0003_subtask_remove_task_tasks_task_sub_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='sub_tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='sub_tasks',
            field=models.ManyToManyField(blank=True, to='tasks_app.subtask'),
        ),
    ]