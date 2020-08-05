from typing import Union


class Config(object):
    __slots__ = ['action', 'ports', 'device_groups', 'flows']

    def __init__(self, ports=[], device_groups=[], flows=[]):
        self.action = 'CONFIGURE'
        self.ports = ports
        self.device_groups = device_groups
        self.flows = flows

    