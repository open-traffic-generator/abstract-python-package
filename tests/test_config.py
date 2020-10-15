import pytest
from abstract_open_traffic_generator.config import Config, Options
from abstract_open_traffic_generator.port import Options as PortOptions


def test_config(serializer, tx, rx, port_ipv4_traffic):
    config = Config(ports=[tx], flows=[port_ipv4_traffic])
    print(serializer.json(config))

def test_config_options(serializer):
    options = Options(PortOptions(location_preemption=True))
    config = Config(options=options)
    print(serializer.json(config))


if __name__ == '__main__':
    pytest.main(['-s', __file__])
