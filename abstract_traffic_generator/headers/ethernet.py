from typing import *


class Ethernet(object):
    """Ethernet traffic header
    """

    def __init__(self, src: str = '000000000000', dst: str = '000000000000', eth_type: str = '0800'):
        self.type = 'ETHERNET'
        self.src = src
        self.dst = dst
        self.eth_type = eth_type

