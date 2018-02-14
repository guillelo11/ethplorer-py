from .client import Client


class Address(Client):
    ADDRESS_INFO = '/getAddressInfo/'
    ADDRESS_HISTORY = '/getAddressHistory/'
    ADDRESS_TRANSACTIONS = '/getAddressTransactions/'

    def __init__(self, address=''):
        Client.__init__(self)
        self.address = address

    def get_address_info(self):
        """
        Returns address info

        {
            address: # address,
            ETH: {   # ETH specific information
                balance:  # ETH balance
                totalIn:  # Total incoming ETH value
                totalOut: # Total outgoing ETH value
            },
            contractInfo: {  # exists if specified address is a contract
                creatorAddress:  # contract creator address,
                transactionHash: # contract creation transaction hash,
                timestamp:       # contract creation timestamp
            },
            tokenInfo:  # exists if specified address is a token contract address (same format as token info),
            tokens: [   # exists if specified address has any token balances
                {
                    tokenInfo: # token data (same format as token info),
                    balance:   # token balance (as is, not reduced to a floating point value),
                    totalIn:   # total incoming token value
                    totalOut:  # total outgoing token value
                },
                ...
            ],
            countTxs:    # Total count of incoming and outcoming transactions (including creation one),
        }
        :return:
        """
        self.build_url(self.ADDRESS_INFO, self.address)
        return self.connect()

    def get_address_history(self):
        """
        Returns the address' history

        {
            operations: [
                {
                    timestamp:       # operation timestamp
                    transactionHash: # transaction hash
                    tokenInfo:       # token data (same format as token info),
                    type:            # operation type (transfer, approve, issuance, mint, burn, etc),
                    address:         # operation target address (if one),
                    from:            # source address (if two addresses involved),
                    to:              # destination address (if two addresses involved),
                    value:           # operation value (as is, not reduced to a floating point value),
                },
                ...
            ]
        }
        :return:
        """
        self.build_url(self.ADDRESS_HISTORY, self.address)
        return self.connect()

    def get_address_transactions(self):
        """
        Returns the address' transactions

        [
            {
                timestamp:       # operation timestamp
                from:            # source address (if two addresses involved),
                to:              # destination address (if two addresses involved),
                hash:            # transaction hash
                value:           # ETH value (as is, not reduced to a floating point value),
                input:           # input data
                success:         # true if transactions was completed, false if failed
            },
        ]
        :return:
        """
        self.build_url(self.ADDRESS_TRANSACTIONS, self.address)
        return self.connect()
