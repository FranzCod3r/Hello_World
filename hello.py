
# A simple repository test

class Hello:
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def __str__(self):
        return f"Hi my name is {self.name}, {self.message}"

hello = Hello("Franz", "I'm learning Python")

print(hello)
