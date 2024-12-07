from main.services.schemas.base_schema import BaseSchema


class Role(BaseSchema):
    """
    The schema class represents a role that user could have.
    """

    id: int
    name: str
    description: str | None


class RoleRspDTO(Role):
    """
    The schema class represents a role response DTO object.
    """

    pass
