import fresh_tomatoes
import media

allmovies,animation,scifi,action = 0,1,2,3
#print(allmovies)

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc","4",[allmovies,animation])
avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=cRdxXPV9GNQ","5",[allmovies,scifi])

interstellar = media.Movie("Interstellar",
                     "A movie about planets and life",
                     "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                     "https://www.youtube.com/watch?v=zSWdZVtXT7E","4",[allmovies,scifi])
#print(toy_story.title)

#avatar.show_trailer()
#print(avatar.categories)
movies = [toy_story, avatar, interstellar]
fresh_tomatoes.open_movies_page(movies)
#print(interstellar.show_trailer().__name__)
