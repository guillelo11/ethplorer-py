from .client import Client


class Transaction(Client):

    TX_INFO = '/getTxInfo/'

    def __init__(self, hash=''):
        Client.__init__(self)
        self.hash = hash

    def get_transaction_info(self):
        self.build_url(self.TX_INFO, self.hash)
        return self.connect()
