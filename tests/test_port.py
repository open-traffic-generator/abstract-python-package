import unittest
import json
import sys
import os
sys.path.insert(-1, os.path.abspath('../abstract_traffic_generator'))
from abstract_traffic_generator.port import *


class TestPackage(unittest.TestCase):
    def test_port(self):
        name = "Abstract Test Port"
        port = Port(name=name, location=Location())
        assert(port.name == name)

    def test_physical_port(self):
        name = "Abstract Test Port"
        physical = Physical(address='127.0.0.1', board=1, port=1)
        port = Port(name=name, location=Location(physical))
        print(json.dumps(port, indent=2, default=lambda x: x.__dict__))
        assert(port.name == name)
        assert(port.location.choice == 'physical')
        assert(port.location.physical.address == '127.0.0.1')


if __name__ == '__main__':
    unittest.main()
