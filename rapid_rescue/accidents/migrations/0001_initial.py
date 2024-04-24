# Generated by Django 5.0.2 on 2024-04-23 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accidents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accident_date', models.DateField(blank=True, null=True)),
                ('accident_time', models.TimeField(blank=True, null=True)),
                ('video_clip', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Accidents',
            },
        ),
        migrations.CreateModel(
            name='Severity',
            fields=[
                ('severity_id', models.AutoField(primary_key=True, serialize=False)),
                ('severity_level', models.IntegerField(blank=True, null=True)),
                ('severity_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Severity',
            },
        ),
    ]