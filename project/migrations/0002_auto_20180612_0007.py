# Generated by Django 2.0.6 on 2018-06-12 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('timestamp',), 'verbose_name': 'project', 'verbose_name_plural': 'projects'},
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
