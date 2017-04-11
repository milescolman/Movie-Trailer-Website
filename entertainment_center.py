import fresh_tomatoes
import media

# Generate the movie objects to list:
# hunger games and avatar were in the udacity example (we like the same movies)
hunger_games = media.Movie("Hunger Games",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  #NOQA
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")  #NOQA

district_9 = media.Movie("District 9",
                  "https://upload.wikimedia.org/wikipedia/en/d/d7/District_nine_ver2.jpg",  #NOQA
                  "https://www.youtube.com/watch?v=DyLUwOcR5pk")  #NOQA
                  
avatar = media.Movie("Avatar",
               "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  #NOQA
               "http://www.youtube.com/watch?v=-9ceBgWV8io")  #NOQA


movies = [avatar, district_9, hunger_games]

# generate and open the HTML for the movie page
fresh_tomatoes.open_movies_page(movies)
