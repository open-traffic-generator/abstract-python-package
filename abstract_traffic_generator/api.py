from typing import Union
from abstract_traffic_generator.config import Config
# from transmit import Transmit
# from capture import Capture
# from flap import Flap


class Api(object):
    def __init__(self):
        pass

    def connect(self, **kwargs):
        """Abstract connect rpc.

        Implementers should override this method and provide 
        their own connection parameters.
        Connection parameters are not specified in the abstract as they are
        transport dependent.
        This allows implementers to specify their transport of choice. 
        """
        raise NotImplementedError()

    def control(self, payload: Union[Config]):
        """Control the traffic generator.

        Args
        ----
        payload (Union[Config, Transmit, Capture, Flag]:
        """
        raise NotImplementedError()
