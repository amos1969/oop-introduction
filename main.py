import random

from user import User

class Main:
    def __init__(self):
        self.people = []
        names = ["Dave", "Karen", "Connor", "Andy", "Helen"]
        for name in names:
            self.people.append(User(name, random.randint(0, 60)))

    def show_people(self):
        for person in self.people:
            print(person)


if __name__ == "__main__":
    main = Main()
    main.show_people()
