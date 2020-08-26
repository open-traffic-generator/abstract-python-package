import pytest


def test_choice(serializer):
    from abstract_open_traffic_generator.flow import Flow, Endpoint, PortEndpoint
    try:
        flow = Flow(name='test', endpoint=PortEndpoint())
        assert('Expected a TypeError when assigning physical')
    except TypeError as e:
        print(e)
        pass

def test_string(serializer):
    from abstract_open_traffic_generator.port import Port
    try:
        port = Port(name=1)
        assert('Expected a TypeError when assigning name')
    except TypeError as e:
        print(e)
        pass

if __name__ == '__main__':
    pytest.main(['-s', __file__])
