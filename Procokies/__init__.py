import os

def get_cookie_string():
    # Path of cookies.txt inside Procokies folder
    cookie_path = os.path.join(os.path.dirname(__file__), "cookies.txt")
    with open(cookie_path, "r") as f:
        return f.read()
