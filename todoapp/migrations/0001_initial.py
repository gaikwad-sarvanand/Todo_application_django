# Generated by Django 4.1.4 on 2023-01-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('finish_at', models.TimeField()),
            ],
            options={
                'db_table': 'Todo',
            },
        ),
    ]