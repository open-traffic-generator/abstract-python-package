import unittest
import json
from abstract_traffic_generator import *


class TestApi(unittest.TestCase):
    def test_connect(self):
        api = Api()
        try:
            api.connect()
            assert('Incorrect behavior')
        except NotImplementedError:
            pass

    def test_control_config(self):
        api = Api()
        config = Config()
        try:
            api.control(payload=config)
            assert('Incorrect behavior')
        except NotImplementedError:
            pass


if __name__ == '__main__':
    unittest.main()
