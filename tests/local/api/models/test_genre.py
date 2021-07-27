import pytest
from local.api.models import Genre


@pytest.mark.django_db
def test_genre_name_max_length_set():
    genre = Genre.objects.create(name="thriller")

    max_length = genre._meta.get_field('name').max_length

    assert max_length == 200

@pytest.mark.django_db
def test_genre_name_str():
    genre = Genre.objects.create(name="thriller")

    s = genre.__str__()

    assert s == "thriller"


