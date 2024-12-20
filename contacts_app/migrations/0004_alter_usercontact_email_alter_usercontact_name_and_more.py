# Generated by Django 5.1.2 on 2024-11-18 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_app', '0003_alter_usercontact_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='usercontact',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usercontact',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
