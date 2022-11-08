from .supply_system import SupplySystem
from .purchase_data import PurchaseData
from .connection_api import ConnectionAPI


class SupplyWriter(ConnectionAPI):
    """
    将读取的数据进行写入
    """
    def __init__(self, supply_sys: SupplySystem) -> None:
        self.supply_sys = supply_sys

    def write_all(self, p_data: PurchaseData):
        """
        实现supply写入数据的方法
        :param p_data:
        :return:
        """
        pass

    def write_part(self, p_data:PurchaseData, batch_num: int):
        """
        部分数据同步到supply

        Args:
            p_data (PurchaseData): _description_
            batch_num(int):同步的数据条目
        :param p_data:
        :param batch_num:
        :return:
        """
        pass
