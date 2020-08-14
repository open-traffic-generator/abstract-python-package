import pytest
from abstract_open_traffic_generator.port import *


def test_default_port(serializer):
    name = 'Default Port'
    port = Port(name=name)
    print(serializer.json(port))
    assert(port.name == name)
    assert(port.location is None)

def test_physical_port(serializer):
    name = "Physical Port"
    physical = Physical(address='127.0.0.1', board=1, port=1)
    port = Port(name=name, location=Location(physical))
    print(serializer.json(port))
    assert(port.name == name)
    assert(port.location.choice == 'physical')
    assert(port.location.physical.address == '127.0.0.1')


if __name__ == '__main__':
    pytest.main(['-s', __file__])
