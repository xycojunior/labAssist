# Generated by Django 5.1 on 2024-08-28 23:32

import auth_user.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0003_alter_user_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', auth_user.managers.UserManager()),
            ],
        ),
    ]
