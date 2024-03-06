class Song:
    
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        
        
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
   
    @classmethod  
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            
    @classmethod  
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(self, genre):
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(self, artist):
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")

# Accessing attributes
print(ninety_nine_problems.name)   # Output: 99 Problems
print(ninety_nine_problems.artist)  # Output: Jay-Z
print(ninety_nine_problems.genre)   # Output: Rap

# Accessing class attributes
print(Song.count)          # Output: 1
print(Song.artists)   # Output: ['Jay-Z']
print(Song.genre_count)    # Output: ['Rap']
