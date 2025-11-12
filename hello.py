
# A simple repository test

#advanced "Hello World":

class Hello:
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def __str__(self):
        return f"Hi my name is {self.name}, {self.message}"

hello = Hello("Franz", "I'm learning Python")

print(hello)


#Classic version:

print("Hi my name is Franz, I'm learning Python")
