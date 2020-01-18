
class Board:

    def __init__(self):

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def get_category(self, position: int):
        if position == 0:
            return 'Pop'
        if position == 4:
            return 'Pop'
        if position == 8:
            return 'Pop'
        if position == 1:
            return 'Science'
        if position == 5:
            return 'Science'
        if position == 9:
            return 'Science'
        if position == 2:
            return 'Sports'
        if position == 6:
            return 'Sports'
        if position == 10:
            return 'Sports'
        return 'Rock'

    def get_question(self, category):
        if category == 'Pop':
            return self.pop_questions.pop(0)
        if category == 'Science':
            return self.science_questions.pop(0)
        if category == 'Sports':
            return self.sports_questions.pop(0)
        if category == 'Rock':
            return self.rock_questions.pop(0)

