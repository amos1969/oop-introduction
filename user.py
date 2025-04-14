class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1

    def __str__(self):
        return f"User: {self.name} - {self.age}"

if __name__ == "__main__":
    me = User("Dave", 55)
    print(f"{me}")