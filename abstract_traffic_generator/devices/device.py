from typing import *
from abstract_traffic_generator.devices.ethernet import Ethernet


class Device(object):
    def __init__(self, 
        name: str,
        parent: str, 
        devices_per_port: int,
        protocols: List[Union[Ethernet]]):
        self.name = name
        self.ports = ports
        self.devices_per_port = devices_per_port
        self.protocols = protocols
