def greet(**kwargs):
    print(f"Hello, {kwargs.get('name', 'Guest')}")

def greet_person(**kwargs):
    greet(**kwargs)

greet_person(name="Bob")
