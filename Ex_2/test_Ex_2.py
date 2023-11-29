import pytest
from Ex_2 import main


def test_Ex_2(mocker):
    inputs = mocker.patch("builtins.input")
    inputs.side_effect = ['104', '1', '200', '1', '100', '1', '100', '2']

    total_pedido = main()

    assert total_pedido == 37.0


if __name__ == '__main__':
    pytest.main()


