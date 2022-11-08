class SyncerException(Exception):
    pass


class ConnectionError(SyncerException):
    """
    当需要连接的系统无法连接时，报错
    """


class ERPConnectionError(ConnectionError):
    """
    ERP无法连接时，抛出异常
    """
    pass