# Generated by Django 5.1.2 on 2024-11-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0006_alter_task_assigned_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(default='', max_length=255),
        ),
    ]
