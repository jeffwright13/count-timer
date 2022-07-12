import pytest
from counters import counters


def pytest_configure():
    pytest.SLEEPER = 0.25
    pytest.MULTIPLIER = 4
    pytest.DURATION = pytest.MULTIPLIER * pytest.SLEEPER
    pytest.REL_TOL = 0.05
    pytest.ABS_TOL = 0.05


@pytest.fixture
def count_timer_zero_duration() -> counters.CountTimer:
    return counters.CountTimer()


@pytest.fixture
def count_timer_nonzero_duration() -> counters.CountTimer:
    return counters.CountTimer()
