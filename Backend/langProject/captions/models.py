from django.db import models

# Create your models here.


class Caption(models.Model):
    video_id = models.CharField(max_length=12)
    start_time = models.FloatField(max_length=12)
    end_time = models.FloatField(max_length=12)
    caption = models.CharField(max_length=100)

    def __str__(self):
        return "Starting at time %s Reads %s" % (self.start_time, self.caption)


class Word(models.Model):
    video_id = models.CharField(max_length=12)
    segment_start_time = models.FloatField(max_length=12)  # start time of segment that contains the word
    word = models.CharField(max_length=20)

    def __str__(self):
        return "%s is available at %d in video %s" % (self.word, self.segment_start_time, self.video_id)


# example to copy for easy input into interactive

"""
if __name__ == '__maicn__':
    print("RUN")
    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "langProject.settings")

    #from captions.models import Caption
    t = Caption(video_id='UID', start_time='000', end_time='124', caption='Captions This is')
    Caption.objects.all()
"""