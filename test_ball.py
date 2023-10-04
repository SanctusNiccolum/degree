"""Test"""

import pytest
from ball import degree

test = (
    ((4, 3, 4, 12), 311),
    ((1, 2, 4, 2), 42),
    ((8, 3, 7, 0), 65),
    ((0, 3, 7, 0), 0)
)


@pytest.mark.parametrize('source, expected', test)
def test_degree(source: tuple[float], expected: int):
    """Test function.

    Args:
        source (tuple[float]): data for test.
        expected (int): expected values.
    """
    assert degree(*source) == expected
