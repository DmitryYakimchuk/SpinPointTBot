from enum import Enum


class Gender(str, Enum):
    """The enumeration is used to represent gender"""

    MALE = "MALE"
    FEMALE = "FEMALE"


class Hand(str, Enum):
    RIGHT = "ПРАВАЯ"
    LEFT = "ЛЕВАЯ"


class Style(str, Enum):
    ATTACKING = "АТАКУЮЩИЙ"
    DEFENSIVE = "ЗАЩИТНЫЙ"
    MIXED = "СМЕШАННЫЙ"
    MASCULINE = "МУЖСКОЙ"
    FEMININE = "ЖЕНСКИЙ"
    SEXLESS = "БЕСПОЛЫЙ"
    CLUMSY = "КОРЯВЫЙ"
    UGLY = "СТРЁМНЫЙ"
    NERVOUS = "НЕРВНЫЙ"
    CALM = "СПОКОЙНЫЙ"


class Level(str, Enum):
    BEGINNER = "НОВИЧОК"
    AMATEUR = "ЛЮБИТЕЛЬ"
    ADVANCED = "ПРОДВИНУТЫЙ"
    EXPERT = "ЭКСПЕРТ"
    LEGEND = "ЛЕГЕНДА"
