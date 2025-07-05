# Procokies/__init__.py

def get_cookie_string():
    with open("cookies.txt", "r") as f:
        return f.read()
