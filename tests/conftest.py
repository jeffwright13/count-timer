import pytest
from counters import counters


def pytest_configure():
    pytest.SLEEPER = 0.25
    pytest.MULTIPLIER = 4
    pytest.DURATION = pytest.MULTIPLIER * pytest.SLEEPER
    pytest.REL_TOL = 0.05
    pytest.ABS_TOL = 0.05


@pytest.fixture
def countup_timer_zero_duration() -> counters.CountupTimer:
    return counters.CountupTimer()


@pytest.fixture
def countup_timer_nonzero_duration() -> counters.CountupTimer:
    return counters.CountupTimer()


@pytest.fixture
def countdown_timer() -> counters.CountdownTimer:
    return counters.CountdownTimer(10)
