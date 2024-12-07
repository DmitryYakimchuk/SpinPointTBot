import aiohttp
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from main.services.schemas.base_schema import BaseSchema
from main.settings import settings

main_handlers = Router()


class Role(BaseSchema):
    """The schema class represents a role that person could have."""

    id: int
    name: str
    description: str | None


@main_handlers.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command.
    """
    await message.answer(f"Hello, {message.from_user.full_name}!")  # type: ignore

    async with aiohttp.ClientSession() as session:
        response = await session.get(f"{settings.BACKEND_API}persons/role")
        roles = await response.json()
        result = "List of roles:\n"
        for role in roles:
            result += f"{Role.model_validate(role).name},\n"
        await message.answer(f"{result};\n")


@main_handlers.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all
    message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
