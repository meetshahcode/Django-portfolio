# Generated by Django 4.0.4 on 2022-05-30 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0008_alter_work_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='gitbool',
            new_name='Gitbool',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='gitlink',
            new_name='Gitlink',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='image',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='livebool',
            new_name='Livebool',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='livelink',
            new_name='Livelink',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='work_id',
            new_name='Work_id',
        ),
    ]