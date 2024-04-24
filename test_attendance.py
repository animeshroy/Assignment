import pytest
from attendance import process

@pytest.mark.parametrize("N, expected_result", [
    (5, '14/29'),
    (10, '372/773')
])
def test_attendance_ways(N, expected_result):
    assert  process(N) == expected_result

