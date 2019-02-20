from django.db import models

class CaptionSegment(models.Model):
    video_id = models.ForeignKey('Video', on_delete=models.CASCADE)
    start_time = models.FloatField(max_length=12)
    end_time = models.FloatField(max_length=12)
    caption = models.CharField(max_length=100)

    def __str__(self):
        return "Starting at time %s Reads %s" % (self.start_time, self.caption)


class Word(models.Model):
    video_id = models.ForeignKey('Video', on_delete=models.CASCADE)
    start_time = models.ForeignKey('CaptionSegment', on_delete=models.CASCADE)  # start time of segment that contains the word
    word = models.CharField(max_length=20)

    def __str__(self):
        return "%s is available at %d in video %s" % (self.word, self.segment_start_time, self.video_id)


class Video(models.Model):
    title = models.CharField(max_length=144)
    video_id = models.CharField(max_length=11)

    def __str__(self):
        return "Title: %s, Video ID: %s" % (title, video_id)

class Subtitle(models.Model):
    language = models.CharField(max_length=3)
    video_id = models.ForeignKey('Video', on_delete=models.CASCADE)

    def __str__(self):
        return "ID: %s, Language: %s" % (video_id, language)




