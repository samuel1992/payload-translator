from operators import GetField

from .payload_translator import PayloadTranslator


def test_a_simple_dict_translate():
    movies = {
        'horror_movie': 'The exorcist',
        'comedy_movie': 'Hitch',
        'war_movie': 'The Rescue of the private Ryan'
    }

    expected_payload = {
        'my_favorite_movie': movies['war_movie'],
        'my_second_favorite_movie': movies['comedy_movie']
    }

    favorite_movies = {
        'my_favorite_movie': GetField('war_movie'),
        'my_second_favorite_movie': GetField('comedy_movie')
    }

    translated_payload = PayloadTranslator(_from=movies,
                                           _to=favorite_movies).translate()

    assert translated_payload == expected_payload
