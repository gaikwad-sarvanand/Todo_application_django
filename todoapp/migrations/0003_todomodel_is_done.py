# Generated by Django 4.1.4 on 2023-01-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_remove_todomodel_finish_at_todomodel_finish_by_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]