import typing


class Port(object):
    """Port class
    """

    def __init__(self, name: str = None, location: str = None):
        self.name = name
        self.location = location
