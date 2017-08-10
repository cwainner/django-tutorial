# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
  artist = models.CharField(max_length=256)
  album_title = models.CharField(max_length=512)
  genre = models.CharField(max_length=128)
  album_logo = models.CharField(max_length=1000)

class Song(models.Model):
  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  file_type = models.CharField(max_length=16)
  song_title = models.CharField(max_length=256)