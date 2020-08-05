from typing import *
from abstract_traffic_generator.devices.device import Device


class DeviceGroup(object):
    def __init__(self, 
        name: str,
        ports: List[str], 
        devices: List[Device]):
        self.name = name
        self.ports = ports
        self.devices = devices
        