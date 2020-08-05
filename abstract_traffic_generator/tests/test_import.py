import unittest
import json
from abstract_traffic_generator import *


class TestPackage(unittest.TestCase):
    def test_package_import(self):
        port = Port("port")
        flow = Flow("flow", endpoint=PortEndpoint(port.name),
            packet=[Ethernet(), Vlan(), Ipv4()])
        config = Config(ports=[port], flows=[flow])
        api = Api()
        print(json.dumps(config, indent=2, default=lambda x: x.__dict__))
        assert(config.action == 'CREATE')
        assert(config.ports[0].name == port.name)
        assert(config.flows[0].name == flow.name)
        assert(config.flows[0].endpoint.type == 'PORT')

    def test_api_methods(self):
        api = Api()
        try:
            api.connect()
            assert('Incorrect behavior')
        except NotImplementedError:
            pass
        try:
            config = Config()
            api.control(payload=config)
            assert('Incorrect behavior')
        except NotImplementedError:
            pass


if __name__ == '__main__':
    unittest.main()
