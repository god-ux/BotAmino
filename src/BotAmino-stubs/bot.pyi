from typing import (
    Any,
    Literal,
    overload
)
from aminofix import ACM, SubClient
from aminofix.lib.util.objects import ThreadList
from .botamino import BotAmino

__all__ = ('Bot',)


class Bot(SubClient, ACM):
    def __init__(
        self,
        client: BotAmino,
        community: int | str,
        prefix: str = "!",
        bio: list[str] | str | None = None,
        activity: bool = False
    ) -> None:
        self.client: BotAmino
        self.prefix: str
        self.bio_contents: list[str] | str | None
        self.activity: bool
        self.marche: bool
        self.language: str
        self.community_amino_id: str
        self.community_id: int
        self.community_leader_agent_id: str
        self.community_name: str
        self.community_leaders: list[str]
        self.community_curators: list[str]
        self.community_staff: list[str]
        self.banned_words: list[str]
        self.locked_command: list[str]
        self.message_bvn: str | None
        self.welcome_chat: str | None
        self.favorite_users: list[str]
        self.favorite_chats: list[str]
        self.new_users: list[str]
    def parse_headers(self, data: str | None = None, type: str | None = None) -> dict[str, Any]: ...
    @property
    def community_filename(self) -> str: ...
    def create_community_file(self) -> None: ...
    def update_file(self, data: dict[str, Any] | None = None) -> None: ...
    def create_dict(self) -> dict[str, Any]: ...
    def get_dict(self) -> dict[str, Any]: ...
    @overload
    def get_file_info(self, key: Literal["prefix"]) -> str: ...
    @overload
    def get_file_info(self, key: Literal["welcome", "welcome_chat"]) -> str | None: ...
    @overload
    def get_file_info(self, key: Literal["banned_words", "favorite_users", "favorite_chats", "locked_command"]) -> list[str]: ...
    def get_file_dict(self) -> dict[str, Any]: ...
    def get_banned_words(self) -> list[str]: ...
    def set_prefix(self, prefix: str) -> None: ...
    def set_welcome_message(self, message: str) -> None: ...
    def set_welcome_chat(self, chatId: str) -> None: ...
    def add_favorite_users(self, value: list[str] | str) -> None: ...
    def add_favorite_chats(self, value: list[str] | str) -> None: ...
    def add_banned_words(self, words: list[str] | str) -> None: ...
    def add_locked_command(self, commands: list[str] | str) -> None: ...
    def remove_favorite_users(self, value: list[str] | str) -> None: ...
    def remove_favorite_chats(self, value: list[str] | str) -> None: ...
    def remove_banned_words(self, words: list[str] | str) -> None: ...
    def remove_locked_command(self, commands: list[str] | str) -> None: ...
    def unset_welcome_chat(self) -> None: ...
    def is_in_staff(self, uid: str) -> bool: ...
    def is_leader(self, uid: str) -> bool: ...
    def is_curator(self, uid: str) -> bool: ...
    def is_agent(self, uid: str) -> bool: ...
    def copy_bubble(self, chatId: str, replyId: str, comId: int | None = None) -> None: ...
    @overload
    def accept_role(self, rid: str) -> bool: ...
    @overload
    def accept_role(self, rid: str, chatId: str | None) -> bool: ...
    def get_staff(self, comIdOrAminoId: int | str) -> list[str]: ...
    def get_user_id(self, name_or_id: str) -> tuple[str, str] | None: ...
    def ask_all_members(self, message: str, lvl: int = 20, type_bool: Literal[1, 2, 3] = 1) -> None: ...
    def ask_amino_staff(self, message: str) -> None: ...
    def stop_instance(self) -> None: ...
    def start_instance(self) -> None: ...
    def leave_amino(self) -> None: ...
    def check_new_member(self) -> None: ...
    def welcome_new_member(self) -> None: ...
    def feature_chats(self) -> None: ...
    def feature_users(self) -> None: ...
    def update_bot_profile(self) -> None: ...
    def get_member_level(self, uid: str) -> int: ...
    def get_member_titles(self, uid: str) -> list[dict[Literal['title', 'color'], str]]: ...
    def get_wallet_amount(self) -> int: ...
    def generate_transaction_id(self) -> str: ...
    @overload
    def pay(self, coins: int, *, blogId: str, transactionId: str | None = None) -> None: ...
    @overload
    def pay(self, coins: int, *, chatId: str | None = None, transactionId: str | None = None) -> None: ...
    @overload
    def pay(self, coins: int, *, objectId: str | None = None, transactionId: str | None = None) -> None: ...
    @overload
    def favorite(self, time: Literal[1, 2, 3] = 1, *, userId: str) -> None: ...
    @overload
    def favorite(self, time: Literal[1, 2, 3] = 1, *, chatId: str) -> None: ...
    @overload
    def favorite(self, time: Literal[1, 2, 3] = 1, *, blogId: str) -> None: ...
    @overload
    def favorite(self, time: Literal[1, 2, 3] = 1, *, wikiId: str) -> None: ...
    @overload
    def unfavorite(self, *, userId: str) -> None: ...
    @overload
    def unfavorite(self, *, chatId: str) -> None: ...
    @overload
    def unfavorite(self, *, blogId: str) -> None: ...
    @overload
    def unfavorite(self, *, wikiId: str) -> None: ...
    @overload
    def join_chatroom(self, chat: str) -> bool: ...
    @overload
    def join_chatroom(self, *, chatId: str) -> bool: ...
    def start_voice_chat(self, chatId: str) -> None: ...  # type: ignore
    def end_voice_chat(self, chatId: str) -> None: ...  # type: ignore
    def start_avatar_chat(self, chatId: str) -> None: ...  # type: ignore
    def end_avatar_chat(self, chatId: str) -> None: ...  # type: ignore
    def start_video_chat(self, chatId: str) -> None: ...  # type: ignore
    def end_video_chat(self, chatId: str) -> None: ...  # type: ignore
    def start_screen_room(self, chatId: str) -> None: ...  # type: ignore
    def end_screen_room(self, chatId: str) -> None: ...  # type: ignore
    def join_voice_chat(self, chatId: str) -> None: ...  # type: ignore
    def join_avatar_chat(self, chatId: str) -> None: ...  # type: ignore
    def join_video_chat(self, chatId: str) -> None: ...  # type: ignore
    def join_screen_room(self, chatId: str) -> None: ...  # type: ignore
    def fetch_channel(self, chatId: str) -> None: ...  # type: ignore
    def get_chats(self, type: str = "recommended", start: int = 0, size: int = 250) -> ThreadList: ...
    def join_all_chat(self) -> None: ...
    def leave_all_chats(self) -> None: ...
    def follow_user(self, uid: list[str] | str) -> None: ...
    def unfollow_user(self, uid: str) -> None: ...
    def add_title(self, uid: str, title: str, color: str | None = None) -> None: ...
    def remove_title(self, uid: str, title: str) -> None: ...
    def passive(self) -> None: ...
