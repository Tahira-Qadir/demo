# Generated by Django 5.0.3 on 2024-03-23 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_userrole_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrole',
            name='image',
        ),
    ]