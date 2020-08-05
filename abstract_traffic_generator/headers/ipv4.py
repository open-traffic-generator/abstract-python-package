from typing import *

class Counter(object):
    def __init__(self):
        self.type = 'COUNTER'

class Random(object):
    def __init__(self):
        self.type = 'RANDOM'

class RepeatableRandom(object):
    def __init__(self):
        self.type = 'REPEATABLE_RANDOM'

class DefaultPhb(object):
    """Default per hop behavior

    Args
    ----
    default (Union[int, List[int], Counter, Random]): Default per hop value
    """
    def __init__(self, 
        default: Union[int, List[int], Counter, Random, RepeatableRandom] = 0,
        unused: Union[int, List[int], Counter, Random, RepeatableRandom] = 0):
        self.type = 'DEFAULT'
        self.default = default
        self.unused = unused


class Dscp(object): 
    """Differentiated services code point ip priority
    
    Args
    ----
    phb (str): Per hop behavior
    """
    def __init__(self, 
        phb: Union[DefaultPhb, 'CLASS_SELECTOR', 'ASSURED_FWD', 'EXPIDITED_FWD'] = DefaultPhb()):
        self.type = 'DSCP'
        self.phb = phb


class Tos(object):
    """Type of service ip priority
    """
    def __init__(self):
        self.type = 'TOS'


class Raw(object):
    """Raw ip priority
    """
    def __init__(self):
        self.type = 'RAW'


class Ipv4(object):
    """Ipv4 traffic header
    """
    def __init__(self, 
        src: str = '0.0.0.0', 
        dst: str = '0.0.0.0', 
        priority: Union[Dscp, Tos, Raw] = Dscp()):
        self.type = 'IPV4'
        self.src = src
        self.dst = dst
        self.priority = priority

