class Port(object):
    __slots__ = ['name', 'location']

    def __init__(self, name=None, location=None):
        self.name = name
        self.location = location
