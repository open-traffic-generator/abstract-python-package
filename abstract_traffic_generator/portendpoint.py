from typing import *


class PortEndpoint(object):
    """Port endpoint represents endpoints for raw traffic over ports

    Args
    ----
    tx (str): Unique name of a tx port. Port.name
    rx (List(str)): Unique names of intended rx ports. Port.name
    """

    def __init__(self, tx: str, rx: List[str] = []):
        self.type = 'PORT'
        self.tx = tx
        self.rx = rx
    