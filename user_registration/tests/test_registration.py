from src.registration import register_user


def test_successful_registration(monkeypatch):

    answers = iter([
        "bharath123",
        "bharath@gmail.com",
        "data_scientist"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(answers)
    )

    assert register_user() is True


def test_invalid_username(monkeypatch):

    answers = iter([
        "admin",
        "bharath@gmail.com",
        "data_scientist"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(answers)
    )

    assert register_user() is False


def test_registration_with_default_handle(monkeypatch):

    answers = iter([
        "bharath123",
        "bharath@gmail.com",
        ""
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(answers)
    )

    assert register_user() is True


def test_invalid_email(monkeypatch):

    answers = iter([
        "bharath123",
        "invalidemail",
        "data_scientist"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(answers)
    )

    assert register_user() is False


def test_invalid_handle(monkeypatch):

    answers = iter([
        "bharath123",
        "bharath@gmail.com",
        "123invalid"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(answers)
    )

    assert register_user() is False
