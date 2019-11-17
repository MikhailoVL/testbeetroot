def admin():
    print("You are good")


def loggedin():
    print("you are almost good")


def unknown():
    print("you are fakckin shet, login and be a good")


permission = {
    "admin": admin,
    "loggedin": loggedin,
    "unknown": unknown
}


class Person:

    def __init__(self, permissions):
        self.permission = permissions
        self.age = Person.get_age()
        self.availabale = self.avaailibale_age()

    @staticmethod
    def get_age():
        return input("Enter age :")

    def avaailibale_age(self):
        if int(self.age) >= 16:
            print("You can look porno")
            return True
        else:
            print("You are small boy, enjoy ")
            return False


vasia = Person("admin")
zina = Person("loggedin")
valdemor = Person("unknown")

permission[vasia.permission]()
permission[zina.permission]()
permission[valdemor.permission]()
