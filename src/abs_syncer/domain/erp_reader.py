import abc
from .connection_api import ConnectionAPI
from .erp_system import ERPSystem
from .purchase_data import PurchaseData


class ERPReader(ConnectionAPI):
    @abc.abstractmethod
    def get_erp_system(self) -> ERPSystem:
        pass

    @abc.abstractmethod
    def read(self) -> PurchaseData:
        """
        返回读取到的erp数据
        :return:
        """
        pass
