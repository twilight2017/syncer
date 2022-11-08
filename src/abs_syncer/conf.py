import pathlib
from dataclasses import dataclass
from typing import Literal


@dataclass
class ERP:
    SERVER_HOST: str
    IS_HTTPS: bool
    username: str
    password: str
    addtID: str
    erptype: Literal["Kingdee"]
    api_endpoint: str
    filter_start_date: str

    @classmethod
    def load_from_dict(cls, data: dict) -> "ERP":
        erp = ERP(
            SERVER_HOST=data["SERVER_HOST"],
            IS_HTTPS=data["IS_HTTPS"],
            username=data["AUTH_INFO"]["username"],
            password=data["AUTH_INFO"]["password"],
            addtID=data["AUTH_INFO"]["addtID"],
            erptype=data["erptype"],
            api_endpoint=data["api_endpoint"],
            filter_start_date=data["filter_start_date"],
        )
        if erp.SERVER_HOST.startswith("http"):
            raise ValueError("Host should be like baidu.com")
        return erp


@dataclass
class SupplySystem:
    name: str
    is_https: bool
    host: str
    api_key: str
    api_endpoint: str
    http_timeout: int

    @classmethod
    def load_from_dict(cls, data: dict) -> "SupplySystem":
        ss = SupplySystem(
            name=data["name"],
            is_https=data["is_https"],
            host=data["host"],
            api_key= data["api_key"],
            api_endpoint=data["api_endpoint"],
            http_timeout=data["http_timeout"],
        )
        if ss.host.startswith("http"):
            raise ValueError("Host should be like baidu.com")
        if not ss.api_endpoint.startswith("/"):
            raise ValueError("api endpoint should start with /")
        return ss


@dataclass
class Config:
    DEBUG: bool
    erp: ERP
    supply_system: SupplySystem
    HTTP_TIMEOUT: int


def load_from_path(path: pathlib.Path) -> Config:
    import yaml

    conf = path.read_text(encoding='utf-8')
    conf_data = yaml.load(conf, Loader=yaml.loader.FullLoader)

    config = Config(
        DEBUG=conf_data["system"]["DEBUG"],
        HTTP_TIMEOUT=conf_data["system"]["HTTP_TIMEOUT"],
        erp=ERP.load_from_dict(conf_data["ERP"]),
        supply_system=SupplySystem.load_from_dict(conf_data["supply"]),
    )
    return config
