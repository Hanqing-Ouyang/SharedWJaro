from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from domainmodel.user import User, Review, Movie
from domainmodel.movie import TestMovieMethods
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

def main():
    #test_article_less_than_operator
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"
    director2 = Director("")
    assert director2.director_full_name is None
    director3 = Director(42)
    assert director3.director_full_name is None

    actor1 = Actor("Angelina Jolie")
    print(actor1)
    assert repr(actor1) == "<Actor Angelina Jolie>"
    actor2 = Actor("")
    print(actor2)
    assert actor2.actor_full_name is None
    actor3 = Actor(42)
    print(actor3)
    assert actor3.actor_full_name is None

    actor3 = Actor("Brad Pitt")
    print(actor3)
    assert repr(actor3) == "<Actor Brad Pitt>"
    actor5 = Actor("Cameron123")
    print(actor5)
    assert repr(actor5) == "<Actor Cameron123>"

    actor3.add_actor_colleague(actor1)
    print(actor3.check_if_this_actor_worked_with(actor1))
    assert (actor3.check_if_this_actor_worked_with(actor1)) == True
    print(actor2.check_if_this_actor_worked_with(actor1))
    assert not (actor2.check_if_this_actor_worked_with(actor1))

    actor3.add_actor_colleague("AA")
    actor3.add_actor_colleague("<Actor None>")
    actor3.add_actor_colleague("<Actor Max>")
    assert repr(actor3._colleagues) == "[<Actor Angelina Jolie>]"
    actor3.add_actor_colleague(Actor("Max"))
    print(actor3._colleagues)
    assert repr(actor3._colleagues) == "[<Actor Angelina Jolie>, <Actor Max>]"
    print(actor1._colleagues)
    assert repr(actor1._colleagues) == "[<Actor Brad Pitt>]"
    print("aaaaaa")
    print(actor3.check_if_this_actor_worked_with("AA"))
    assert not (actor3.check_if_this_actor_worked_with("AA"))
    print(actor3.check_if_this_actor_worked_with(Actor("AA")))
    assert not (actor3.check_if_this_actor_worked_with(Actor("AA")))

    print(actor1.__lt__(actor3))
    assert (actor1.__lt__(actor3))
    print(actor1.__lt__("AA"))
    assert not (actor1.__lt__("AA"))





    #test_Movie
    movie = Movie("Moana", 2016)
    print(movie)
    assert repr(movie) == "<Movie Moana, 2016>"
    director = Director("Ron Clements")
    movie.director = director
    print(movie.director)
    assert repr(movie.director) == "<Director Ron Clements>"
    description= "This movie was very enjoyable."
    movie.description=description
    assert repr(movie.description) == "This movie was very enjoyable."
    actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
    for actor in actors:
        movie.add_actor(actor)
    print(movie.actors)
    assert repr(
        movie.actors) == "[<Actor Auli'i Cravalho>, <Actor Dwayne Johnson>, <Actor Rachel House>, <Actor Temuera Morrison>]"

    movie.runtime_minutes = 107
    print("Movie runtime: {} minutes".format(movie.runtime_minutes))
    assert movie.runtime_minutes == 107

    movie2 = Movie("Moana", 2016)
    print(movie2)
    assert repr(movie) == "<Movie Moana, 2016>"

    movie3 = Movie("Moana", 1996)
    print(movie3)
    assert repr(movie3) == "<Movie Moana, 1996>"

    movie4 = Movie("", 1996)
    print(movie4)
    assert repr(movie4) == "<Movie None, 1996>"

    movie5 = Movie(24, 'abc')
    print(movie5)
    assert repr(movie5) == "<Movie None, None>"

    movie6 = Movie("", 1)
    print(movie6)
    assert repr(movie6) =="<Movie None, None>"

    movie7 = Movie("pkq",1)
    print(movie7)
    assert repr(movie7) == "<Movie pkq, None>"

    movie8 = Movie(1, 1900)
    print(movie8)
    assert repr(movie8) == "<Movie None, 1900>"


    print(movie.__eq__(movie2))
    assert True
    print(movie.__hash__() == movie2.__hash__())
    assert True
    print(movie.__hash__())
    print(movie3.__hash__())
    print(movie.__hash__() == movie3.__hash__())
    assert not (movie.__hash__() == movie3.__hash__())

    movie6.director="aa"
    print(movie6.director)
    assert movie6.director == None
    movie.director = Director("Cameron")
    print(movie.director)
    assert repr(movie.director)== "<Director Cameron>"

    #with movie.raises(ValueError):
    #movie2.runtime_minutes = -10
    #with movie.raises(ValueError):
    #movie3.runtime_minutes = "abcd"

    movie4.runtime_minutes = 120
    print(movie3.runtime_minutes)
    print("movie2.runtime_minutes",movie2.runtime_minutes)
    movie.add_genre(Genre("Horror"))
    print(movie.genres)
    assert repr(movie.genres) == "[<Genre Horror>]"
    movie.add_genre("NotGenre")
    print(movie.genres)
    assert repr(movie.genres) == "[<Genre Horror>]"
    movie.remove_genre(Genre("aa"))
    print(movie.genres)
    assert repr(movie.genres) == "[<Genre Horror>]"
    movie.remove_genre(Genre("Horror"))
    print(movie.genres)
    assert repr(movie.genres) == "[]"

    movie.add_actor(Actor("Jaro"))
    print(movie.actors)
    assert repr(
        movie.actors) == "[<Actor Auli'i Cravalho>, <Actor Dwayne Johnson>, <Actor Rachel House>, <Actor Temuera Morrison>, <Actor Jaro>]"

    movie.remove_actor(Actor("Auli'i Cravalho"))
    print(movie.actors)
    assert repr(
        movie.actors) == "[<Actor Dwayne Johnson>, <Actor Rachel House>, <Actor Temuera Morrison>, <Actor Jaro>]"



if __name__ == "__main__":
        main()