# Generated by Django 5.1.2 on 2024-11-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_app', '0004_alter_usercontact_email_alter_usercontact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontact',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='usercontact',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='usercontact',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]
