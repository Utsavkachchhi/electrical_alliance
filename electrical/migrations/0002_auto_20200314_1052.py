# Generated by Django 2.0.8 on 2020-03-14 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electrical', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='image',
            new_name='Image',
        ),
    ]