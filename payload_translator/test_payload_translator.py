from .operators import GetFrom, Join
from .payload_translator import PayloadTranslator

MOVIES = {
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


def test_a_nested_dict_translate():
    favorite_movies = {
        'horror': {
            'name': GetFrom('horror_movie'),
        },
        'speed_movies': [
            {'name': GetFrom('car_movie')},
            {'name': GetFrom('motorcycle_movie')}
        ],
        'dramas': [GetFrom(('dramas', 'romantic_drama')),
                   GetFrom(('dramas', 'tragedy_drama'))]

    }

    expected_payload = {
        'horror': {
            'name': MOVIES['horror_movie']
        },
        'speed_movies': [
            {'name': MOVIES['car_movie']},
            {'name': MOVIES['motorcycle_movie']}
        ],
        'dramas': [MOVIES['dramas']['romantic_drama'],
                   MOVIES['dramas']['tragedy_drama']]
    }

    translated_payload = PayloadTranslator(_from=MOVIES,
                                           _to=favorite_movies).translate()

    assert expected_payload == translated_payload


def test_a_dict_translate():
    car_and_motorcycle = f"{MOVIES['car_movie']}, {MOVIES['motorcycle_movie']}"
    expected_payload = {
        'my_favorite_movie': MOVIES['war_movie'],
        'my_second_favorite_movie': MOVIES['comedy_movie'],
        'my_third_favorite_movie': MOVIES['dramas']['romantic_drama'],
        'my_movies_of_velocity': car_and_motorcycle
    }

    favorite_movies = {
        'my_favorite_movie': GetFrom('war_movie'),
        'my_second_favorite_movie': GetFrom('comedy_movie'),
        'my_third_favorite_movie': GetFrom(('dramas', 'romantic_drama')),
        'my_movies_of_velocity': Join('car_movie',
                                      'motorcycle_movie',
                                      delimiter=', ')
    }

    translated_payload = PayloadTranslator(_from=MOVIES,
                                           _to=favorite_movies).translate()

    assert translated_payload == expected_payload
