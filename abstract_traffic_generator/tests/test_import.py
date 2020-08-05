import unittest
from abstract_traffic_generator import *


class TestPackage(unittest.TestCase):
    def test_package_import(self):
        port = Port()
        flow = Flow()
        config = Config()
        api = Api()

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
