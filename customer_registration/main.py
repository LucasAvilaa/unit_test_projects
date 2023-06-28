MINIMUM_AGE = 18
EMAIL_CHARACTER = "@"
MINIMUM_SIZE_NAME = 3

class Costumer():
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


class System():

    def __init__(self):
        self.list_costumer = []

    def create_costumer(self, costumer):
        self.list_costumer.append(costumer)

        if costumer.age < MINIMUM_AGE:
            return "Minor, not registered"
        
        if EMAIL_CHARACTER not in costumer.email:
            return "Invalid email, not registered"

        if len(costumer.name) < MINIMUM_SIZE_NAME:
            return "Invalid name, not registered"
        
        if costumer in self.list_costumer:
            return "Registered successfully"