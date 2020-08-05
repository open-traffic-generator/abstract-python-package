from typing import Union


class Config(object):
    """Control the configuration
    """

    def __init__(self, action: Union['CREATE', 'UPDATE']='CREATE', 
        ports=[], device_groups=[], flows=[]):
        self.action = action
        self.ports = ports
        self.device_groups = device_groups
        self.flows = flows

    