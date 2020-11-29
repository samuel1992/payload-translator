from .operators import GetField, GetSubField
from .payload_translator import PayloadTranslator


def test_a_dict_translate():
    movies = {
        'horror_movie': 'The exorcist',
        'comedy_movie': 'Hitch',
        'war_movie': 'The Rescue of the private Ryan',
        'dramas': {
            'romantic_drama': 'silver linings playbook',
            'tragedy_drama': 'marley and me'
        }
    }

    expected_payload = {
        'my_favorite_movie': movies['war_movie'],
        'my_second_favorite_movie': movies['comedy_movie'],
        'my_third_favorite_movie': movies['dramas']['romantic_drama']
    }

    favorite_movies = {
        'my_favorite_movie': GetField('war_movie'),
        'my_second_favorite_movie': GetField('comedy_movie'),
        'my_third_favorite_movie': GetSubField(('dramas', 'romantic_drama'))
    }

    translated_payload = PayloadTranslator(_from=movies,
                                           _to=favorite_movies).translate()

    assert translated_payload == expected_payload
