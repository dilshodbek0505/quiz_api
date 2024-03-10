from enum import Enum

class AnswerWord(Enum):
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'

    @classmethod
    def get_choices(cls):
        return [(i.name, i.value) for i in cls]