# Generated by Django 3.1.1 on 2020-09-05 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GenApi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gen',
            old_name='related_disease',
            new_name='diseases',
        ),
    ]