import fresh_tomatoes
import media

#assiging values to different genres
allmovies,animation,scifi,action,comedy,education = 0,1,2,3,4,5


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

threeidiots = media.Movie("3 idiots",
                     "3 Idiots is a 2009 Indian comedy-drama education based film",
                     "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                     "https://www.youtube.com/watch?v=xvszmNXdM4w","4",[allmovies,comedy,education])

herapheri = media.Movie("Hera Pheri",
                     "Hera Pheri is a 2000 Indian comedy thriller film",
                     "https://upload.wikimedia.org/wikipedia/en/5/51/Hera_Pheri_%28poster%29.jpg",
                     "https://www.youtube.com/watch?v=1rJQQCZcq2s","4",[allmovies,comedy,education])

logan = media.Movie("Logan",
                     "Logan is a 2017 American superhero film",
                     "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                     "https://www.youtube.com/watch?v=Div0iP65aZo","4",[allmovies,scifi])


#movies list
movies = [avatar, interstellar,threeidiots,herapheri,logan,toy_story]

#open_movies_page from the fresh_tomatoes formats and writes the code in html file and open it in browser
fresh_tomatoes.open_movies_page(movies)

