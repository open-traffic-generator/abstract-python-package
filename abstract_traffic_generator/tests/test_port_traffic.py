import unittest
import json
from abstract_traffic_generator import *


class TestTraffic(unittest.TestCase):
    def test_port_traffic(self):
        tx = Port(name='Tx Port', location='1.1.1.1/1/1')
        rx = Port(name='Rx Port', location='1.1.1.1/1/2')
        background = Flow(name='Background Traffic', endpoint=PortEndpoint(tx=tx.name),
            packet=[Ethernet(), Vlan(), Ipv4()])
        pfc = Flow(name='Pfc Traffic', endpoint=PortEndpoint(tx=tx.name),
            packet=[PfcPause()])
        config = Config(ports=[tx, rx], flows=[background, pfc])
        print(json.dumps(config, indent=2, default=lambda x: x.__dict__))
        assert(len(config.ports) == 2)
        assert(len(config.flows) == 2)

    def test_device_traffic(self):
        pass

if __name__ == '__main__':
    unittest.main()
