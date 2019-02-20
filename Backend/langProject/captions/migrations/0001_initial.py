# Generated by Django 2.1.7 on 2019-02-17 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=12)),
                ('start_time', models.FloatField(max_length=12)),
                ('end_time', models.FloatField(max_length=12)),
                ('caption', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=12)),
                ('segment_start_time', models.FloatField(max_length=12)),
                ('word', models.CharField(max_length=20)),
            ],
        ),
    ]
