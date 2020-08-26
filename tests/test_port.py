import pytest
from abstract_open_traffic_generator.port import *


def test_default_port(serializer):
    name = 'Default Port'
    port = Port(name=name)
    print(serializer.json(port))
    assert(port.name == name)
    assert(port.location is None)

def test_physical_port(serializer):
    name = 'Physical Port'
    location = '127.0.0.1;1;1'
    port = Port(name=name, location=location)
    print(serializer.json(port))
    assert(port.name == name)
    assert(port.location == location)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
