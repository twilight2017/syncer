from dataclasses import dataclass
from typing import Any


@dataclass
class DataColumn:
    """
    必填字段
    """
    sys_name: str  # 供应协同名称
    erp_name: str  # erp名称
    mytype: Any  # 字段类型

    def check_type(self, data):
        return  isinstance(data, self.mytype)


@dataclass
class DataMappint:
    data_column = DataColumn
    erp_var_name: str  # ERP系统中的字段名
