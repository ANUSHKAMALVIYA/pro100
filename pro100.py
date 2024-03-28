class MovieRating:
    def __init__(self, movie_name, story_rating, actor_rating, music_rating):
        self.movie_name = movie_name
        self.story_rating = story_rating
        self.actor_rating = actor_rating
        self.music_rating = music_rating
        self.avg_rating = (story_rating + actor_rating + music_rating) / 3

    def __str__(self):
        stars = '*' * int(round(self.avg_rating))
        return f"Thanks for the response, You rated {self.movie_name} with {stars}\n" \
               f"{{'Movie Name': '{self.movie_name}', 'story rating': {self.story_rating}, " \
               f"'Actor Rating': {self.actor_rating}, 'Music Rating': {self.music_rating}, " \
               f"'Avg Rating': {self.avg_rating}"


# Example usage:
movie1 = MovieRating('Good life', 1, 1, 3)
print(movie1)

movie2 = MovieRating('Beautiful Sound', 5, 5, 5)
print(movie2)

movie3 = MovieRating('Red Apple', 2, 3, 5)
print(movie3)
