from typing import Any, BinaryIO
from typing_extensions import Literal

from .client import Client
from .lib.util import (
    CommunityList,
    CommunityStats,
    JoinRequest,
    NoticeList,
    UserProfile,
    UserProfileList
)

__all__ = ("ACM",)


class ACM(Client):
    def __init__(self, profile: UserProfile, comId: int) -> None:
        self.comId: int
    def create_community(
        self,
        name: str,
        tagline: str,
        icon: BinaryIO,
        themeColor: str,
        joinType: int = 0,
        primaryLanguage: str = "en"
    ) -> Literal[200]: ...
    def delete_community(self, email: str, password: str, verificationCode: str) -> Literal[200]: ...
    def list_communities(self, start: int = 0, size: int = 25) -> CommunityList: ...
    def get_categories(self, start: int = 0, size: int = 25) -> dict[str, Any]: ...
    def change_sidepanel_color(self, color: str) -> dict[str, Any]: ...
    def upload_themepack_raw(self, file: BinaryIO) -> dict[str, Any]: ...
    def promote(self, userId: str, rank: str) -> Literal[200]: ...
    def get_join_requests(self, start: int = 0, size: int = 25) -> JoinRequest: ...
    def accept_join_request(self, userId: str) -> Literal[200]: ...
    def reject_join_request(self, userId: str) -> Literal[200]: ...
    def get_community_stats(self) -> CommunityStats: ...
    def get_community_user_stats(self, type: Literal["curator", "leader"], start: int = 0, size: int = 25) -> UserProfileList: ...
    def change_welcome_message(self, message: str, isEnabled: bool = True) -> Literal[200]: ...
    def change_guidelines(self, message: str) -> Literal[200]: ...
    def edit_community(
        self,
        name: str | None = None,
        description: str | None = None,
        aminoId: str | None = None,
        primaryLanguage: str | None = None,
        themePackUrl: str | None = None
    ) -> Literal[200]: ...
    def change_module(
        self,
        module: Literal["catalog", "chat", "externalcontent", "featured", "featuredchats", "featuredposts", "featuredusers", "influencer", "leaderboards", "livechat", "posts", "publicchats", "ranking", "screeningroom", "sharedfolder", "topiccategories"],
        isEnabled: bool
    ) -> Literal[200]: ...
    def add_influencer(self, userId: str, monthlyFee: int) -> Literal[200]: ...
    def remove_influencer(self, userId: str) -> Literal[200]: ...
    def get_notice_list(self, start: int = 0, size: int = 25) -> NoticeList: ...
    def delete_pending_role(self, noticeId: str) -> Literal[200]: ...