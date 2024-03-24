"""
PyTests for: users.foobar, 
Commands...
> pytest  // run pytest on code
> coverage run -m pytest [test_users.py]  // generate .coverage file
> coverage report  // reads from .coverage
(Can also run flake8, after pip install, with > flake8 <file>)
"""

import numpy as np
import pytest  # evaluates all funcs and methods with a test_ prefix or _test suffix

from src.utils.users import foobar


def test_foobar():

    # VALID (SUNNY) TESTS
    assert foobar(np.array([1, 7]), np.array([1, 3])) == 22  # array inputs
    assert foobar((1, 7), np.array([1, 3])) == 22            # tuple input
    assert foobar([1, 7], np.array([1, 3])) == 22            # list input

    assert foobar([1, 7], [1, 3]) == 22                 # int vals
    assert foobar([1.0, 7.0], [1, 3]) == 22.0           # float vals
    assert foobar([0, 0], [1, 3]) == 0                  # zero vals
    assert foobar([1, -7], [-1, 3]) == -22              # neg vals
    assert foobar([1e30, 7e30], [1e10, 3e-30]) == 1e40  # large vals

    np.testing.assert_array_equal(foobar(np.eye(1000), np.eye(1000)), np.eye(1000))  # large dims
    np.testing.assert_array_equal(foobar([[[10, 0], [5, 2]], [[2, 3], [3, 3]]],      # mult dims
                                         [[[10, 0], [5, 2]], [[2, 3], [3, 3]]]),
                                  [[[100, 0], [60, 4]], [[13, 15], [15, 18]]])

    # ERROR (RAINY) TESTS
    with pytest.raises(ValueError):
        assert foobar([1, 2], [1, 1, 1])                       # mismatch dims
    with pytest.raises(TypeError):
        assert foobar({'first': 1, 'second': 2}, [1, 1]) == 3  # dict input
    with pytest.raises(np.core._exceptions._UFuncNoLoopError):
        assert foobar(['foo', 'bar'], [1, 1])                  # str vals
