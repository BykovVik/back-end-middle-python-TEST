# Generated by Django 4.2.5 on 2023-10-01 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_customuser_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=32),
        ),
    ]
