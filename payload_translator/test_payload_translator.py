from .operators import GetFrom, Join
from .payload_translator import PayloadTranslator


def test_a_dict_translate():
    movies = {
        'car_movie': 'Fast And Furious',
        'motorcycle_movie': 'easy rider',
        'horror_movie': 'The exorcist',
        'comedy_movie': 'Hitch',
        'war_movie': 'The Rescue of the private Ryan',
        'dramas': {
            'romantic_drama': 'silver linings playbook',
            'tragedy_drama': 'marley and me'
        }
    }

    car_and_motorcycle = f"{movies['car_movie']}, {movies['motorcycle_movie']}"
    expected_payload = {
        'my_favorite_movie': movies['war_movie'],
        'my_second_favorite_movie': movies['comedy_movie'],
        'my_third_favorite_movie': movies['dramas']['romantic_drama'],
        'my_movies_of_velocity': car_and_motorcycle
    }

    favorite_movies = {
        'my_favorite_movie': GetFrom('war_movie'),
        'my_second_favorite_movie': GetFrom('comedy_movie'),
        'my_third_favorite_movie': GetFrom(('dramas', 'romantic_drama')),
        'my_movies_of_velocity': Join(GetFrom('car_movie'),
                                      GetFrom('motorcycle_movie'),
                                      delimiter=', ')
    }

    translated_payload = PayloadTranslator(_from=movies,
                                           _to=favorite_movies).translate()

    assert translated_payload == expected_payload
