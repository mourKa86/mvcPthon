from enum import Enum

class ColorTheme(Enum):
    LIGHT = 1
    DEFAULT = 2
    DARK = 3

    @classmethod
    def values(cls):
        return cls([str(member.value) for member in ColorTheme])
        # return cls(list(map(int, ColorTheme)))


    @classmethod
    def names(cls):
        return cls([member.name for member in ColorTheme])

    @classmethod
    def result(cls):
        return cls([(member.name, member.value) for member in ColorTheme])