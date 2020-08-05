from typing import *
from abstract_traffic_generator.portendpoint import PortEndpoint
from abstract_traffic_generator.headers.ethernet import Ethernet
from abstract_traffic_generator.headers.vlan import Vlan
from abstract_traffic_generator.headers.ipv4 import Ipv4
 


class Flow(object):
    """Flow
    """

    def __init__(self, name: str, endpoint: Union[PortEndpoint],
        packet: List[Union[Ethernet, Vlan, Ipv4]] = [Ethernet()]):
        self.name = name
        self.endpoint = endpoint
        self.packet = packet

    