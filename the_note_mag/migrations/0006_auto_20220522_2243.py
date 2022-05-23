# Generated by Django 3.2 on 2022-05-22 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_note_mag', '0005_alter_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Music', 'Music'), ('Live', 'Live'), ('Review', 'Review'), ('Playlist', 'Playlist')], default='Music', max_length=50),
        ),
    ]