from artists.models import Artist, Song


def task_1_artists_filter_by_popularity():
    """Should return all artists that have more than 80 popularity"""
    artist = Artist.objects.filter(popularity__gt=80)
    return artist

def task_2_artists_get_by_artistic_name():
    """Should return the artist which artistic name is Jimi Hendrix"""
    artist = Artist.objects.get(artistic_name='Jimi Hendrix')
    return artist


def task_3_songs_delete():
    """Should delete all songs that contain any letter 't' in its title"""
    Song.objects.filter(title__contains='t').delete()


def task_4_artists_create_song():
    """Should create a new song for B.B. King artist"""
    artist = Artist.objects.get(artistic_name='B.B. King')
    Song.objects.create(artist_id=artist.id, title='New Song', album_name='New Album')

def task_5_artists_order_by_popularity():
    """Should return all artists ordered by popularity"""
    artist = Artist.objects.all().order_by('popularity')
    return artist

def task_6_song_edit_album():
    """Should take the song with title 'Superstition' and update its album name with any other name"""
    song = Song.objects.get(title='Superstition')
    song.album_name = "Any other name"
    song.save()

def task_7_song_counter():
    """Should return the amount of songs stored in the database"""
    return Song.objects.all().count()
