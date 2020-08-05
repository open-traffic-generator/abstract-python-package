from typing import *


class Vlan(object):
    """Vlan traffic header
    
    Any None value will indicate that the default on the server will be used.

    Args
    ----
    protocol (str): Tag protocol identifier
    priority (int): Priority code point
    cfi (int): Canonical format indicator or Drop elegible indicator
    id (int): Vlan identifier
    """

    def __init__(self, 
        protocol: str = '8100',
        priority: int = None, 
        cfi: int = None, 
        id: int = None):
        self.type = 'VLAN'
        self.protocol = protocol
        self.priority = priority
        self.cfi = cfi
        self.id = id

