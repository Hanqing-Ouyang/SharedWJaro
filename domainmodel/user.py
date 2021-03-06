from domainmodel.movie import Movie
from domainmodel.review import Review

class User:
    pass

    def __init__(
            self, user_name: str, password: str
    ):
        if user_name == "" or type(user_name) is not str:
            self._user_name = None
        else:
            self._user_name = user_name.strip().lower()
        self._password: str=  password
        self._watched_movies=[]
        self._reviews=[]
        self._time_spent_watching_movies_minutes= 0

    @property
    def user_name(self) -> str:
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        if user_name == "" or type(user_name) is not str:
            self._user_name = None
        else:
            self._user_name = user_name.strip().lower()

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password):
        if type(password) is str:
            self._password = password.strip()

    @property
    def watched_movies(self) -> list():
        return self._watched_movies

    @watched_movies.setter
    def actors(self, watched_movies):
        self._watched_movies = watched_movies

    @property
    def reviews(self) -> list():
        return self._reviews

    @reviews.setter
    def reviews(self, reviews):
        self._reviews = reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self._time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def runtime_minutes(self, time_spent_watching_movies_minutes):
        if type(time_spent_watching_movies_minutes) is int:
            if int(time_spent_watching_movies_minutes) > 0:
                self._time_spent_watching_movies_minutes = time_spent_watching_movies_minutes

    def __repr__(self):
        return f'<User {self._user_name}>'

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return (
            other._user_name == self._user_name
            )

    def __lt__(self, other):
        if isinstance(other, User):
            return ((self._user_name) < (other._user_name))

    def __hash__(self):
        ty = str(self._user_name)
        return hash(ty)

    def watch_movie(self,movie:Movie):
        if isinstance(movie, Movie):
            self._watched_movies.append(movie)
            self._time_spent_watching_movies_minutes= self._time_spent_watching_movies_minutes+movie.runtime_minutes

    def add_review(self,review:Review):
        if isinstance(review, Review):
            self._reviews.append(review)

    def remove_review(self,comment:str,movie:Movie):
        for i in self._reviews:
            if (i._review_text== comment) and (i._movie== movie):
                self._reviews.remove(i)


class TestuserMethods:

    def test_init(self):
        # test User
        user1 = User('Martin', 'pw12345')
        user2 = User('Ian', 'pw67890')
        user3 = User('Daniel', 'pw87465')
        print(user1)
        assert repr(
            user1) == "<User martin>"
        print(user2)
        assert repr(
            user2) == "<User ian>"
        print(user3)
        assert repr(
            user3) == "<User daniel>"