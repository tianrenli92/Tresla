# Generated by Django 2.0.6 on 2018-06-11 19:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectMembers',
            new_name='ProjectMember',
        ),
    ]