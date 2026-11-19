
import pytest

from src.prime import is_prime


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (11, True),
        (13, True),
        (17, True),
        (19, True),
        (23, True),
        (29, True),

        (0, False),
        (1, False),
        (-1, False),
        (-5, False),

        (4, False),
        (6, False),
        (8, False),
        (9, False),
        (10, False),
        (15, False),
        (21, False),
        (25, False),
        (100, False),
    ]
)
def test_is_prime(number, expected):
    assert is_prime(number) is expected


def test_large_prime():
    assert is_prime(997) is True


def test_large_non_prime():
    assert is_prime(1000) is False



def test_large_prime_number():
    assert is_prime(104729) is True
