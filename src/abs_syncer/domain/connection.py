import enum
from dataclasses import dataclass
from typing import Any, Optional


class Status(enum.IntEnum):
    success = 1
    failed = 0


@dataclass
class Connection:
    """
    connection status of ERP system
    """
    status: Status  # 连接状态
    host: str  # 连接的host地址
    api: str  # 连接的api接口
    msg: str  # 连接提示信息

    error_dict = Optional[dict] = None
    api_key = Optional[str] = None

    def is_connected(self) -> bool:
        return self.status == Status.success

    def information(self) -> str:
        return f"Connection informaton: host:{self.host}, api:{self.api}, msg:{self.msg}"
