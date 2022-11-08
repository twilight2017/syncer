from .connection import Connection
from dataclasses import dataclass


@dataclass
class SupplySystem:
    host: str
    api_key: str
    version: str

    def check_connection(self) -> Connection:
        """
        检查供应协同系统的可用性
        :return:
        """
        return NotImplemented('not implement')

    def auth(self) -> bool:
        """
        鉴权，判断链接是否正常
        Raises: NotImplemented: _description_

        Returns:
            bool: 链接状态
        :return:
        """
        return NotImplemented('not implement')