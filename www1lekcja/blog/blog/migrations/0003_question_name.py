# Generated by Django 4.1.1 on 2022-09-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]