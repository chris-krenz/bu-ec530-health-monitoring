import pytest  # evaluates all funcs and methods with a test_ prefix or _test suffix

from src.utils.misc.sanitizer import sanitizer


def test_sanitizer():

    # Sunny Tests
    assert sanitizer('Sunny test') == 'Submitted message clean...'

    # Rainy Tests
    with pytest.raises(RuntimeError):
        assert sanitizer('select this rainy test;')
