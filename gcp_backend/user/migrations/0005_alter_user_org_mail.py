# Generated by Django 4.1.4 on 2022-12-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_org_id_user_org_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='org_mail',
            field=models.CharField(default='abcd', max_length=100),
        ),
    ]