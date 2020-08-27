import pytest
from abstract_open_traffic_generator.flow import *


def test_pfc_pause_default(serializer):
    pfc = PfcPause()
    print(serializer.json(pfc))


def test_pfc_pause_custom(serializer):
    pfc = PfcPause(src=Pattern('000001000001'),
        class_enable_vector=Pattern('0x0101'),
        pause_class_0=Pattern('0x0001'),
        pause_class_4=Pattern(Counter(start='0', step='1', count=5)))
    print(serializer.json(pfc))


if __name__ == '__main__':
    pytest.main(['-s', __file__])
