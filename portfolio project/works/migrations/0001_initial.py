# Generated by Django 4.0.4 on 2022-05-30 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='works',
            fields=[
                ('image', models.ImageField(upload_to='images/')),
                ('works_id', models.AutoField(primary_key=True, serialize=False)),
                ('summary', models.TextField()),
            ],
        ),
    ]
