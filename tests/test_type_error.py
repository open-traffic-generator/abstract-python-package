import pytest
from abstract_open_traffic_generator.port import *


def test_choice(serializer):
    physical = {
        'address': '127.0.0.1', 
        'board': 1, 
        'port': 1
    }
    try:
        port = Port(name='test', location=Location(physical))
        assert('Expected a TypeError when assigning physical')
    except TypeError as e:
        print(e)
        pass

def test_string(serializer):
    try:
        port = Port(name=1)
        assert('Expected a TypeError when assigning name')
    except TypeError as e:
        print(e)
        pass

if __name__ == '__main__':
    pytest.main(['-s', __file__])
