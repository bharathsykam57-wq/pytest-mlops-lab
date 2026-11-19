import pytest
from src.validators import (
    validate_username,
    validate_email,
    validate_handle,
)
from src.validators import resolve_handle

def test_valid_username():
    assert validate_username("bharath123") is True


def test_empty_username():
    assert validate_username("") is False


def test_username_with_spaces():
    assert validate_username("bharath kumar") is False


def test_banned_username():
    assert validate_username("admin") is False


def test_banned_username_case_insensitive():
    assert validate_username("ADMIN") is False
    
    
@pytest.mark.parametrize(
    "email, expected",
    [
        ("student@gmail.com", True),
        ("user@university.fr", True),
        ("invalidemail", False),
        ("user@gmail", False),
        ("usergmail.com", False),
        ("", False),
    ]
)
def test_validate_email(email, expected):
    assert validate_email(email) is expected
    
@pytest.mark.parametrize(
    "handle, expected",
    [
        ("bharath_123", True),
        ("dataScientist", True),
        ("ab", False),
        ("a" * 21, False),
        ("123bharath", False),
        ("_bharath", False),
        ("bharath-name", False),
        ("bharath name", False),
        ("admin", False),
        ("ROOT", False),
    ]
)
def test_validate_handle(handle, expected):
    assert validate_handle(handle) is expected
    
    
def test_default_handle():
    assert resolve_handle("bharath123", "") == "bharath123"


def test_custom_handle():
    assert resolve_handle("bharath123", "data_scientist") == "data_scientist"