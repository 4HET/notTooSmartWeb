# Generated by Django 4.1.1 on 2022-09-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Punch', '0002_rename_name_user_password_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='2659335014@qq.com', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='isPunch',
            field=models.BooleanField(default=False),
        ),
    ]
