from django.db import models

class CaptionSegment(models.Model):
    video_id = models.ForeignKey('Video', to_field='video_id', on_delete=models.CASCADE)
    start_time = models.FloatField(max_length=12)
    end_time = models.FloatField(max_length=12)
    caption = models.CharField(max_length=100)

    def __str__(self):
        return "Starting at time %s Reads %s" % (self.start_time, self.caption)


class Word(models.Model):
    video_id = models.ForeignKey('Video', to_field='video_id', on_delete=models.CASCADE)
    caption_segment_id = models.ForeignKey('CaptionSegment', on_delete=models.CASCADE)
    word = models.CharField(max_length=20)

    def __str__(self):
        return "%s is available at %d in video %s" % (self.word, self.segment_start_time, self.video_id)


class Video(models.Model):
    title = models.CharField(max_length=144)
    video_id = models.CharField(unique=True, max_length=11)

    def __str__(self):
        return "Title: %s, Video ID: %s" % (self.title, self.video_id)


class Subtitle(models.Model):
    language = models.CharField(max_length=3)
    video_id = models.ForeignKey('Video', to_field='video_id', on_delete=models.CASCADE)

    def __str__(self):
        return "ID: %s, Language: %s" % (self.video_id, self.language)




