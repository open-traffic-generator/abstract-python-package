from typing import *
from abstract_traffic_generator.portendpoint import PortEndpoint
from abstract_traffic_generator.headers.ethernet import Ethernet
from abstract_traffic_generator.headers.vlan import Vlan
from abstract_traffic_generator.headers.ipv4 import Ipv4
from abstract_traffic_generator.headers.pfcpause import PfcPause 


class Flow(object):
    """Flow
    """

    def __init__(self, name: str, endpoint: Union[PortEndpoint],
        packet: List[Union[Ethernet, Vlan, Ipv4, PfcPause]] = [Ethernet()]):
        self.name = name
        self.endpoint = endpoint
        self.packet = packet

    