from typing import *


class Ipv4(object):
    """Ipv4 traffic header
    """

    def __init__(self, src: str = '0.0.0.0', dst: str = '0.0.0.0', qos: str = '1'):
        self.type = 'IPV4'
        self.src = src
        self.dst = dst
        self.qos = qos

