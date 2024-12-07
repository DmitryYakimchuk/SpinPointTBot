from uuid import UUID

from main.exceptions.base_exception import ExceptionBase


class UserExceptionBase(ExceptionBase):
    """
    Base exception for user.
    """

    pass


class NoRolesForUserException(UserExceptionBase):
    """
    Exception raised if the role list of the user is empty.
    """

    def __init__(self, user_name: str) -> None:
        self.message = f"The role list for user with name {user_name} is empty."
        super().__init__(self.message)


class PersonNotFoundException(UserExceptionBase):
    """
    Exception raised if user with the given id doesn't exist.
    """

    def __init__(self, id: int) -> None:
        self.message = f"The user with {id=} not found."
        super().__init__(self.message)


class UserNotFoundException(UserExceptionBase):
    """
    Exception raised if user with the given user_id doesn't exist.
    """

    def __init__(self, user_id: UUID) -> None:
        self.message = f"The user with {user_id=} not found."
        super().__init__(self.message)


class NoSelectedRolesForUserException(UserExceptionBase):
    """
    Exception raised if the role_ids list of the user is empty.
    """

    def __init__(self, user_name: str) -> None:
        self.message = f"The role_ids list for user with name {user_name} is empty."
        super().__init__(self.message)
