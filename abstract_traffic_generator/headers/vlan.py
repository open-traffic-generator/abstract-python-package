from typing import *


class Vlan(object):
    """Vlan traffic header
    """

    def __init__(self, id: str = '1', priority: str = '0', cfi: str = '1', protocol: str = 'FFFF'):
        self.type = 'VLAN'
        self.id = id
        self.priority = priority
        self.cfi = cfi
        self.protocol = protocol

