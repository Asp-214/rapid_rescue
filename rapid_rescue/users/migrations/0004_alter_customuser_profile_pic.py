# Generated by Django 5.0.4 on 2024-04-25 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='default_user_pic.jpg', upload_to='profile_pics/'),
        ),
    ]
