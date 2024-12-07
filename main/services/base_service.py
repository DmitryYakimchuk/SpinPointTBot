from abc import ABC
from typing import Generic, TypeVar

from main.services.schemas.base_schema import BaseSchema


SchemaType = TypeVar("SchemaType", bound=BaseSchema)


class BaseService(ABC, Generic[SchemaType]):
    """Base class for all services"""

    pass
