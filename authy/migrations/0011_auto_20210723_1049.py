# Generated by Django 3.2.5 on 2021-07-23 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0010_auto_20210723_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='image',
        ),
        migrations.RemoveField(
            model_name='police',
            name='image',
        ),
        migrations.RemoveField(
            model_name='work',
            name='image',
        ),
    ]