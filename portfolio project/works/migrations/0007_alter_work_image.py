# Generated by Django 4.0.4 on 2022-05-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0006_work_gitbool_work_gitlink_work_livebool_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]