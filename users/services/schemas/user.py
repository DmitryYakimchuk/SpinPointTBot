from typing import Any

from pydantic import UUID4, AwareDatetime, EmailStr, model_validator
from pydantic_extra_types.phone_numbers import PhoneNumber

from main.services.schemas.base_schema import BaseSchema
from users.exceptions.user_exceptions import NoRolesForUserException
from users.services.enums.user_enum import Gender, Hand, Level, Style
from users.services.schemas.role import Role


class User(BaseSchema):
    """
    The schema class represents user data.
    """

    id: int
    user_id: UUID4
    name: str
    email: EmailStr
    telegram_id: str
    phone: PhoneNumber
    gender: Gender
    birthday: AwareDatetime | None
    roles: list[Role]
    about: str | None
    address: str | None  # TODO change to Address schema

    searchable: bool = True
    hand: Hand | None
    style: Style | None
    level: Level | None

    @model_validator(mode="before")
    def validate_roles(cls, values: dict[str, Any]) -> dict[str, Any]:
        roles: list[Role] = values.get("roles", [])
        user_name: str = values.get("name", "Unknown")
        if not roles:
            raise NoRolesForUserException(user_name)
        return values
