from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Artiste(models.Model):
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def getName(self):
     return self.first_name,self.last_name,self.age

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.FloatField()
    
    pass
    
class Song(Artiste):
    def __init__(self, first_name, last_name, age,title,date_released,Artiste,likes,artiste_id):
        super().__init__(first_name, last_name, age)
        self.title = title
        self.date_released = date_released
        self.Artiste = Artiste
        self.likes = likes
        self.artiste_id = artiste_id
       
            

        title = models.CharField(max_length=100, unique=True)
        date_released = models.DateTimeField(auto_now_add=True)
        Artiste =models.ManyToManyField()
        likes = models.ManyToManyField()
        artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
        return self.title,self.ldate_released,self.likes

pass

class Lyrics(Song):
    def __init__(self, first_name, last_name, age, title, date_released, Artiste, artiste_id,content,song_id,obsessions):
        super().__init__(first_name, last_name, age, title, date_released, Artiste, artiste_id)

        self.content = content
        self.date_released = date_released
        self.Artiste = Artiste
        self.song_id = song_id
        self.obsessions = obsessions
        
    
    
        content =models.ManyToManyField()
        song_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
        obsessions = models.ForeignKey(Artiste, to_field='titel', on_delete=models.CASCADE)

        return self.content,self.song_id,self.obsessions
pass
