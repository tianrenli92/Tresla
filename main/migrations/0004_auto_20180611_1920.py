# Generated by Django 2.0.6 on 2018-06-11 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180611_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='owner_id',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='projectmember',
            old_name='member_id',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='projectmember',
            old_name='project_id',
            new_name='project',
        ),
    ]