# Generated by Django 5.0.4 on 2024-04-24 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_user_pic.jpg', null=True, upload_to='profile_pics/'),
        ),
    ]
