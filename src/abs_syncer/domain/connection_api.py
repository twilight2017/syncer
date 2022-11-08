import abc
from .connection import Connection


class ConnectionAPI(abc.ABC):
    @abc.abstractmethod
    def check_connection(self) -> Connection:
        """
        检查链接状态
        :return:
        """
        pass
