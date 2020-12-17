from decimal import Decimal
from .films_api_service import FilmsAPIService
from datetime import datetime


class FilmsDataStatsGenerator(object):

    p1 = FilmsAPIService()
    result = p1.get_all_films()

    def __init__(self, films_api_service):
        self.films_api_service = films_api_service
        print(type(films_api_service))

        # self.result = films_api_service.get_all_films()

    def get_best_rated_film(self, director_name) -> str:
        """TODO Implement
        Retrieves the name of the best rated film that was directed by the director with the given name.
        If there are no films directed the the given director, return the None object.
        Note there will only be one film with the best rating.
        """

        best_film = ""
        best_rating = 0
        result = self.result

        for i in range(len(result)):
            if result[i]['directorName'] == director_name:
                if result[i]['rating'] > best_rating:
                    best_rating = result[i]['rating']
                    best_film = result[i]['name']

        if len(best_film) > 0:
            return best_film
        else:
            return

    def get_director_with_most_films(self) -> str:
        """TODO Implement
        Retrieves the name of the director who has directed the most films in the CodeScreen Film service.
        """
        # p1 = FilmsAPIService()
        # result = p1.get_all_films()

        result = self.result

        directors = []
        for i in range(len(result)):
            directors.append(result[i]['directorName'])

        my_dict = {i: directors.count(i) for i in directors}

        max_movies = 0
        director_most_movies = ""

        for i in directors:
            if (my_dict[i] > max_movies):
                director_most_movies = i
                max_movies = my_dict[i]

        if len(director_most_movies) > 0:
            return director_most_movies
        else:
            return

    def get_average_rating(self, director_name) -> Decimal:
        """TODO Implement
        Retrieves the average rating for the films directed by the given director, rounded to 1 decimal place.
        If there are no films directed the the given director, return the None object.
        """
        # p1 = FilmsAPIService()
        sum_ratings = 0
        avg_rating = 0
        counter = 0
        # result = p1.get_all_films()

        result = self.result

        for i in range(len(result)):
            if result[i]['directorName'] == director_name:
                counter += 1
                sum_ratings += result[i]['rating']
                avg_rating = (sum_ratings/counter)

        if avg_rating > 0:
            return round(avg_rating)
        else:
            return

    def get_shortest_number_of_days_between_film_releases(self, director_name) -> int:
        """TODO Implement
        Retrieves the shortest number of days between any two film releases directed by the given director.
        If there are no films directed by the given director, return the None object.
        If there is only one film directed by the given director, return 0.
        Note that no director released more than one film on any given day."""

        date_format = "%Y-%m-%d"
        p1 = FilmsAPIService()
        result = p1.get_all_films()
        release_date = []
        for i in range(len(result)):
            if result[i]['directorName'] == director_name:
                date = datetime.strptime(result[i]['releaseDate'], date_format)
                release_date.append(date)

        release_date.sort()

        difference_days = 0
        smallest = []

        if(len(release_date) > 1):
            for i in range(len(release_date)-1):
                difference_days = abs(
                    (release_date[i+1] - release_date[i]).days)
                smallest.append(difference_days)
            smallest.sort()
            return smallest[0]
        else:
            return 0

        # For example, if the service returns the following 4 films,
        # {
        #     "name": "Batman Begins",
        #     "length": 140,
        #     "rating": 8.2,
        #     "releaseDate": "2006-06-16",
        #     "directorName": "Christopher Nolan"
        # },
        # {
        #     "name": "Interstellar",
        #     "length": 169,
        #     "rating": 8.6,
        #     "releaseDate": "2014-11-07",
        #     "directorName": "Christopher Nolan"
        # },
        # {
        #     "name": "Prestige",
        #     "length": 130,
        #     "rating": 8.5,
        #     "releaseDate": "2006-11-10",
        #     "directorName": "Christopher Nolan"
        # },
        # {
        #     "name": "Black Hawk Down",
        #     "length": 152,
        #     "rating": 7.7,
        #     "releaseDate": "2001-1-18",
        #     "directorName": "Ridley Scott"
        # }

        # then this method should return 147 for Christopher Nolan, as Prestige was released 147 days after Batman Begins.
        # """
