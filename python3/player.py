
class Player:

    def __init__(self, name: str):
        self.name: str = name

        self.purse = 0
        self.position = 0
        self.in_penalty_box = False
        self.staying_in_penalty_box = True

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name
