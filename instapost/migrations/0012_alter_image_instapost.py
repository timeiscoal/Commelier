# Generated by Django 4.1.1 on 2022-10-04 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instapost', '0011_image_instapost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='instapost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instapost.instapost'),
        ),
    ]
