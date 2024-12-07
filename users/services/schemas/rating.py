from pydantic import UUID4, AwareDatetime, NonNegativeFloat

from main.services.schemas.base_schema import BaseSchema


class Rating(BaseSchema):
    """
    The schema class represents rating of the player.
    """

    id: int
    user_id: UUID4
    date: AwareDatetime
    value: NonNegativeFloat


class RatingRspDTO(Rating):
    """
    The schema class represents rating response DTO.
    """

    pass
