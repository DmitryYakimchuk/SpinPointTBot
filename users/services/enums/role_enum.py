from enum import Enum


class RoleEnum(str, Enum):
    PLAYER = "ИГРОК"
    REFEREE = "СУДЬЯ"
    TRAINER = "ТРЕНЕР"
