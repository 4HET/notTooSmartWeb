# Generated by Django 4.1 on 2022-10-08 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Punch", "0003_user_email_user_ispunch"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user", name="email", field=models.EmailField(max_length=254),
        ),
    ]
