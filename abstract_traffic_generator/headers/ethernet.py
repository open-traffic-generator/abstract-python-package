from typing import *


class Ethernet(object):
    """Ethernet traffic header

    Args
    ----
    dst (str): Destination mac address
    src (str): Source mac address
    eth_type: Ethernet type
    """

    def __init__(self, src: str = None, dst: str = None, eth_type: str = '0800'):
        self.type = 'ETHERNET'
        self.src = src
        self.dst = dst
        self.eth_type = eth_type

