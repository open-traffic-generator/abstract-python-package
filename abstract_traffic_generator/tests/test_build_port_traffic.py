import unittest
import json
from abstract_traffic_generator import *


class TestBuildPortTraffic(unittest.TestCase):
    def test_build_port_traffic(self):
        tx = Port(name='Tx Port', location='1.1.1.1/1/1')
        rx = Port(name='Rx Port', location='1.1.1.1/1/2')
        flow = Flow(name='Tx -> Rx', endpoint=PortEndpoint(tx=tx.name),
            packet=[Ethernet(), Vlan(), Ipv4()])
        config = Config(ports=[tx, rx], flows=[flow])
        print(json.dumps(config, indent=2, default=lambda x: x.__dict__))
        assert(len(config.ports) == 2)
        assert(len(config.flows) == 1)


if __name__ == '__main__':
    unittest.main()
