# Generated by Django 2.1.7 on 2019-02-20 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('captions', '0003_auto_20190220_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='start_time',
            new_name='caption_segment_id',
        ),
    ]
