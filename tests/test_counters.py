import math
import pytest
import time
from counters.counters import (
    CountupTimer,
    CountupTimerWithExpiry,
    CountdownTimer,
)

SLEEPER = 0.25
MULTIPLIER = 4
DURATION = MULTIPLIER * SLEEPER
REL_TOL = 0.05
ABS_TOL = 0.05


@pytest.mark.unit
class TestCountupTimer:
    def test_init(self):
        timer = CountupTimer()
        assert timer._time_started is None
        assert timer._time_paused is None
        assert timer._elapsed == 0
        assert timer.paused is True
        assert timer.running is False

    def test_start(self):
        timer = CountupTimer()
        timer.start()
        assert timer._time_started is not None
        assert timer.paused is False

    def test_reset(self):
        timer = CountupTimer()
        timer.start()
        timer.reset()
        assert timer._time_started is None
        assert timer._time_paused is None
        assert timer.paused is True

    def test_start_twice(self):
        timer = CountupTimer()
        timer.start()
        timer.start()
        assert timer._time_started is not None
        assert timer.paused is False

    def test_pause(self):
        timer = CountupTimer()
        timer.start()
        timer.pause()
        assert timer._time_paused is not None
        assert timer.paused is True
        assert timer.running is False
        assert timer._time_started is not None
        assert timer._time_paused > timer._time_started

    def test_pause_twice(self):
        timer = CountupTimer()
        timer.start()
        timer.pause()
        timer.pause()
        assert timer._time_paused is not None
        assert timer.paused is True
        assert timer.running is False

    def test_pause_while_not_started(self):
        timer = CountupTimer()
        timer.pause()
        assert timer._time_paused is None
        assert timer.paused is True
        assert timer.running is False

    def test_resume(self):
        start = time.time()
        timer = CountupTimer()
        timer.start()
        timer.pause()
        time.sleep(SLEEPER)
        timer.resume()
        assert timer._time_started > start
        assert math.isclose(timer.elapsed, 0.0, abs_tol=ABS_TOL)
        assert timer.paused is False
        assert timer.running is True
        time.sleep(0.1)
        assert math.isclose(timer.elapsed, 0.1, rel_tol=REL_TOL)

    def test_resume_twice(self):
        start = time.time()
        timer = CountupTimer()
        timer.start()
        timer.pause()
        timer.resume()
        timer.resume()
        assert timer._time_started > start
        assert math.isclose(timer.elapsed, 0.0, abs_tol=ABS_TOL)
        assert timer.paused is False
        assert timer.running is True

    def test_resume_not_started(self):
        timer = CountupTimer()
        timer.resume()
        assert timer._time_started is None
        assert timer.paused is True

    def test_elapsed(self):
        timer = CountupTimer()
        timer.start()
        time.sleep(SLEEPER)
        assert math.isclose(timer.elapsed, SLEEPER, rel_tol=REL_TOL)

    def test_get(self):
        timer = CountupTimer()
        timer.start()
        time.sleep(SLEEPER)
        got = timer._get()
        assert got > SLEEPER

    def test_get_with_pause(self):
        timer = CountupTimer()
        timer.start()
        time.sleep(SLEEPER)
        timer.pause()
        time.sleep(SLEEPER)
        got = timer._get()
        assert math.isclose(got, SLEEPER, rel_tol=REL_TOL)

    def test_get_not_started(self):
        timer = CountupTimer()
        got = timer._get()
        assert got == 0


@pytest.mark.unit
class TestCountupTimerWithExpiry:
    def test_start(self):
        timer = CountupTimerWithExpiry(duration=DURATION)
        timer.start()
        assert timer._time_started is not None
        assert timer.paused is False

    def test_expired(self):
        timer = CountupTimerWithExpiry(duration=DURATION)
        timer.start()
        assert timer.expired is False
        time.sleep(SLEEPER + DURATION)
        assert timer.expired is True

    def test_remaining(self):
        timer = CountupTimerWithExpiry(duration=DURATION)
        timer.start()
        assert math.isclose(timer.remaining, DURATION, rel_tol=REL_TOL)
        time.sleep(SLEEPER)
        assert math.isclose(timer.remaining, DURATION - SLEEPER, rel_tol=REL_TOL)


@pytest.mark.unit
class TestCountdownTimer:
    def test_start(self):
        timer = CountdownTimer(duration=DURATION)
        timer.start()
        assert timer._time_started is not None
        assert timer.paused is False

    def test_expired(self):
        timer = CountdownTimer(duration=DURATION)
        timer.start()
        assert timer.expired is False
        assert math.isclose(timer.remaining, DURATION, rel_tol=REL_TOL)
        time.sleep(DURATION + 0.1)  # just barely go beyond the duration
        assert timer.expired is True
        assert timer.remaining == 0

    def test_remaining(self):
        timer = CountdownTimer(duration=DURATION)
        timer.start()
        assert timer.expired is False
        time.sleep(SLEEPER)
        assert math.isclose(timer.remaining, DURATION - SLEEPER, rel_tol=REL_TOL)
        time.sleep(SLEEPER)
        assert math.isclose(timer.remaining, DURATION - 2 * SLEEPER, rel_tol=REL_TOL)
        time.sleep(SLEEPER)
        assert math.isclose(timer.remaining, DURATION - 3 * SLEEPER, rel_tol=REL_TOL)

    def test_pause(self):
        timer = CountupTimer()
        timer.start()
        timer.pause()
        assert timer._time_paused is not None
        assert timer.paused is True
        assert timer.running is False
        assert timer._time_started is not None
        assert timer._time_paused > timer._time_started

    def test_resume(self):
        start = time.time()
        timer = CountupTimer()
        timer.start()
        timer.pause()
        time.sleep(SLEEPER)
        timer.resume()
        assert timer._time_started > start
        assert math.isclose(timer.elapsed, 0, abs_tol=ABS_TOL)
        assert timer.paused is False
        assert timer.running is True
