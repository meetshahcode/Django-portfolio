# Generated by Django 4.0.4 on 2022-05-30 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0007_alter_work_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
