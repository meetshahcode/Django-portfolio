# Generated by Django 4.0.4 on 2022-05-30 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_rename_works_id_works_work_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='works',
            new_name='work',
        ),
    ]
