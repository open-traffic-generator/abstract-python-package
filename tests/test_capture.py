import pytest
from abstract_open_traffic_generator.config import Config
from abstract_open_traffic_generator.port import Port
from abstract_open_traffic_generator.capture import *


def test_capture(serializer):
    """Demonstrate how to specify capture settings for a configuration
    """
    config = Config()
    config.ports.append(Port(name='port1'))
    capture = Capture(name='capture1',
                      port_names=[config.ports[0].name],
                      choice=[
                          BasicFilter(
                              MacAddressFilter('source',
                                               filter='000000000000'))
                      ])
    config.captures.append(capture)
    print(serializer.json(config))


if __name__ == '__main__':
    pytest.main(['-s', __file__])
