from movie_storage import get_movies


def is_movie_in_dict(name, movies):
    """
        Check if a movie title exists in the dictionary in a case-insensitive manner.

        Args:
            name (str): The movie title to check.
            movies (dict): The dictionary of movies, where keys are movie titles.

        Returns:
            bool: True if the movie title exists in the dictionary (case-insensitive), False otherwise.
    """
    return name.lower() in map(lambda key: key.lower(), movies.keys())
    # return title.lower() in map(str.lower(), movies.keys())


def test_is_movie_in_dict():
    assert is_movie_in_dict("pulp", get_movies()) is False


def test_is_movie_in_dict2():
    assert is_movie_in_dict("pulp fiction", get_movies()) is True