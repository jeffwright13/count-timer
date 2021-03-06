"""Configure pytest itself."""


import pytest

from count_timer.count_timer import CountTimer


def pytest_configure():
    """Define constants."""
    pytest.SLEEPER = 0.25
    pytest.MULTIPLIER = 4
    pytest.DURATION = pytest.MULTIPLIER * pytest.SLEEPER
    pytest.REL_TOL = 0.10
    pytest.ABS_TOL = 0.10


@pytest.fixture
def count_timer_zero_duration() -> CountTimer:
    """Return CountTimer of zero duration."""
    return CountTimer()


@pytest.fixture
def count_timer_nonzero_duration() -> CountTimer:
    """Return CountTimer of well-defined duration."""
    return CountTimer(duration=pytest.DURATION)
