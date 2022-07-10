import pytest
from counters import counters


@pytest.fixture
def countup_timer() -> counters.CountupTimer:
    return counters.CountupTimer()


@pytest.fixture
def countup_expiry_timer() -> counters.CountupTimerWithExpiry:
    return counters.CountupTimerWithExpiry(9)


@pytest.fixture
def countdown_expiry_timer() -> counters.CountdownTimer:
    return counters.CountdownTimer(10)


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
# def countdown_expirey_timer(duration, howmany: int=1) -> counters.CountdownTimer:
#     if howmany <= 0:
#         raise ValueError("howmany must be greater than 0")
#     return counters.CountdownTimer(duration) if howmany == 1 else [counters.CountdownTimer(duration) for _ in range(howmany)]
