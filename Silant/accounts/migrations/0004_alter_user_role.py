# Generated by Django 4.2.15 on 2024-08-26 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Manager', 'Менеджер'), ('Client', 'Client'), ('Service Company', 'Service Company')], max_length=15),
        ),
    ]
