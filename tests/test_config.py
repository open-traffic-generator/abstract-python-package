import pytest
from abstract_open_traffic_generator.config import Config


def test_config(serializer, tx, rx, port_ipv4_traffic):
    config = Config(ports=[tx], flows=[port_ipv4_traffic])
    print(serializer.json(config))


if __name__ == '__main__':
    pytest.main(['-s', __file__])
