# Generated by Django 5.1.1 on 2024-09-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='text',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
