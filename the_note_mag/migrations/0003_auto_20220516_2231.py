# Generated by Django 3.2 on 2022-05-16 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_note_mag', '0002_auto_20220516_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
