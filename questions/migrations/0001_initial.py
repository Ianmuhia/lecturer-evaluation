# Generated by Django 2.2.1 on 2019-07-13 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('question_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('question_description', models.TextField(max_length=500)),
                ('question_other', models.TextField(max_length=500)),
            ],
        ),
    ]
