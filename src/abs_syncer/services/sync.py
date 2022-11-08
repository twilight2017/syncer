import enum
from abs_syncer.logger import Logger
from abs_syncer.domain.erp_reader import ERPReader
from abs_syncer.domain.supply_writer import SupplyWriter
from abs_syncer.domain.connection_api import ConnectionAPI
from abs_syncer.exceptions import ConnectionError, SyncerException


class SyncMode(enum.Enum):
    ContinousRead = 1
    Webhook = 2


class SyncReader:
    def __init__(self, reader: ERPReader, logger: Logger, writer: SupplyWriter) -> None:
        self.reader = reader
        self.writer = writer
        self.logger = logger

    def check_connection(self, connector: ConnectionAPI):
        conn = connector.check_connection()
        if not conn.is_connected():
            err_msg = conn.information()
            self.logger.error(err_msg)
            raise ConnectionError(err_msg)

    def do_sync(self, mode: SyncMode = SyncMode.ContinousRead):
        """
        发起轮询同步
        Raises:
        ERPConnectionError: ERP链接错误
        :param mode:
        :return:
        """
        # 首次链接，判断链接是否成功
        self.check_connection(self.writer)

        # 开始同步
        if mode == SyncMode.ContinousRead:
            self.continous_read_and_write()
        elif mode == SyncMode.Webhook:
            raise SyncerException(f'mode name: {mode}, not implemented method.')
        else:
            raise SyncerException(f'mode name: {mode}, Not no such mode')

    def continous_read_and_write(self):
        """
        进入本方法时，连接已经稳定
        :return:
        """
        while True:
            data = self.reader.read()

            # 检查supply的状态
            self.check_connection(self.writer)
            self.writer.write_all(data)
