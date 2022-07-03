import pytest
from counters import counters

@pytest.fixture
def countup_timer() -> counters.CountupTimer:
    return counters.CountupTimer()

@pytest.fixture
def countup_expiry_timer() -> counters.CountupTimerWithExpiry:
    return counters.CountupTimerWithExpiry(9)

@pytest.fixture
def countdown_expiry_timer() -> counters.CountdownTimerWithExpiry:
    return counters.CountdownTimerWithExpiry(10)

# @pytest.fixture
# def countup_timer(howmany: int=1) -> counters.CountupTimer:
#     if howmany <= 0:
#         raise ValueError("howmany must be greater than 0")
#     return counters.CountupTimer() if howmany == 1 else [counters.CountupTimerWithExpiry(howmany) for _ in range(howmany)]

# @pytest.fixture
# def countup_expiry_timer(duration, howmany: int=1) -> counters.CountupTimerWithExpiry:
#     if howmany <= 0:
#         raise ValueError("howmany must be greater than 0")
#     return counters.CountupTimerWithExpiry(duration) if howmany == 1 else [counters.CountupTimerWithExpiry(duration) for _ in range(howmany)]

# @pytest.fixture
# def countdown_expirey_timer(duration, howmany: int=1) -> counters.CountdownTimerWithExpiry:
#     if howmany <= 0:
#         raise ValueError("howmany must be greater than 0")
#     return counters.CountdownTimerWithExpiry(duration) if howmany == 1 else [counters.CountdownTimerWithExpiry(duration) for _ in range(howmany)]
