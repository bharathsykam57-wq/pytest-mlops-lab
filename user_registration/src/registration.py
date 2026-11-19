from src.validators import (
    validate_username,
    validate_email,
    validate_handle,
    resolve_handle,
)


def register_user():

    username = input("Enter username: ")
    email = input("Enter email: ")
    handle = input("Enter handle (optional): ")

    handle = resolve_handle(username, handle)

    if not validate_username(username):
        print("Invalid username")
        return False

    if not validate_email(email):
        print("Invalid email")
        return False

    if not validate_handle(handle):
        print("Invalid handle")
        return False

    print("Registration successful!")
    return True