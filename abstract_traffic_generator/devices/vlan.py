from typing import *


class Vlan(object):
    """Vlan protocol

    Args
    ----
    name (str): Unique name  
    children (str): The protocols that are stacked on top of this protocol  
    protocol (str): Tag protocol identifier  
    priority (int): Priority code point  
    id (int): Vlan identifier  
    """
    def __init__(self, 
        name: str,
        children: List[Union[Vlan, Ipv4, Bgpv4]],
        cfi: str = None,
        priority: str):
        self.type = 'VLAN'
        self.name = name
        self.parent = parent.name
        self.protocol = protocol
        self.priority = priority
        self.id = id
