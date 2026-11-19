def validate_username(username):

    banned_words = {
        "admin",
        "root",
        "moderator",
        "mod",
        "null"
    }

    if not username:
        return False

    if " " in username:
        return False

    if username.lower() in banned_words:
        return False

    return True


def validate_email(email):
    if not email:
        return False

    if "@" not in email:
        return False

    if "." not in email:
        return False

    return True


def validate_handle(handle):

    banned_words = {
        "admin",
        "root",
        "moderator",
        "mod",
        "null"
    }

    # Rule 1: Length must be between 3 and 20
    if len(handle) < 3 or len(handle) > 20:
        return False

    # Rule 2: First character must be a letter
    if not handle[0].isalpha():
        return False

    # Rule 3: Only letters, numbers, and underscores
    if not handle.replace("_", "").isalnum():
        return False

    # Rule 4: Banned words are not allowed
    if handle.lower() in banned_words:
        return False

    return True


def resolve_handle(username, handle):

    if not handle:
        return username

    return handle
