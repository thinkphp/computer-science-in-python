import json

def write_user_data(username, password, filename="user_data.json"):
    """
    Writes username and password to a JSON file.

    Args:
        username (str): The username.
        password (str): The password.
        filename (str, optional): The name of the JSON file. Defaults to "user_data.json".
    """

    user_data = {
        "username": username,
        "password": password
    }

    with open(filename, "w") as f:
        json.dump(user_data, f, indent=4)

# Example usage:
write_user_data("john_doe", "my_secret_password")


def read_user_data(filename="user_data.json"):
    """
    Reads username and password from a JSON file.

    Args:
        filename (str, optional): The name of the JSON file. Defaults to "user_data.json".

    Returns:
        dict: A dictionary containing the username and password.
    """

    with open(filename, "r") as f:
        user_data = json.load(f)

    return user_data

# Example usage:
user_data = read_user_data()
print(user_data["username"])
print(user_data["password"])
