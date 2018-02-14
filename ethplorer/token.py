from .client import Client


class Token(Client):

    TOKEN_INFO = '/getTokenInfo/'
    TOKEN_HISTORY = '/getTokenHistory/'
    TOP_TOKENS = '/getTopTokens'

    def __init__(self, address=''):
        Client.__init__(self)
        self.address = address

    def get_token_info(self):
        self.build_url(self.TOKEN_INFO, self.address)
        return self.connect()

    def get_token_history(self):
        self.build_url(self.TOKEN_HISTORY, self.address)
        return self.connect()

    def get_top_tokens(self):
        self.build_url(self.TOP_TOKENS)
        return self.connect()
        