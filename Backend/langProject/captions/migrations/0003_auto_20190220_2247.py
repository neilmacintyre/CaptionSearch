# Generated by Django 2.1.7 on 2019-02-20 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captions', '0002_auto_20190220_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='id',
        ),
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
    ]
