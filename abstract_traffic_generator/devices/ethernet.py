from typing import *


class Ethernet(object):
    """Ethernet protocol

    Args
    ----
    name (str): Unique name  
    parent (str): The name of another protocol that this protocol 
    will be stacked on top of  
    mac (str): Mac address
    mtu (int): Maximum transmission unit
    """
    def __init__(self, 
        name: str,
        children: List[Union[Vlan, Ipv4]],
        mac: str = None,
        mtu: str = None):
        self.type = 'ETHERNET'
        self.name = name
        self.children = children
        self.mac = mac
        self.mtu = mtu
