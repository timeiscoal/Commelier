# Generated by Django 4.1.1 on 2022-10-04 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instapost', '0003_instacomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instacomment',
            old_name='comment_author',
            new_name='author',
        ),
    ]
