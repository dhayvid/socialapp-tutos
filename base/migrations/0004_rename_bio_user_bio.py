# Generated by Django 4.1 on 2022-08-17 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='bio',
            new_name='Bio',
        ),
    ]
