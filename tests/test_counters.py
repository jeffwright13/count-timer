import math
import time
import pytest
from counters.counters import (
    CountupTimer,
    CountdownTimer,
)


@pytest.mark.unit
class TestCountupTimer:
    def test_init(self, countup_timer_zero_duration):
        timer = CountupTimer()
        assert timer._time_started is None
        assert timer._time_paused is None
        assert timer._elapsed == 0
        assert timer._duration == 0
        assert timer.paused is True
        assert timer.running is False

    def test_init_nonzero_duration(self):
        timer = CountupTimer(duration=pytest.DURATION)
        assert timer._time_started is None
        assert timer._time_paused is None
        assert timer._elapsed == 0
        assert timer._duration == pytest.DURATION
        assert timer.paused is True
        assert timer.running is False

    def test_start(self):
        timer = CountupTimer(duration=pytest.DURATION)
        timer.start()
        assert timer._time_started is not None
        assert timer.paused is False

    def test_reset(self):
        timer = CountupTimer()
        timer.start()
        timer.reset()
        assert timer._time_started is None
        assert timer._time_paused is None
        assert timer._elapsed == 0
        assert timer._duration == 0
        assert timer.paused is True
        assert timer.running is False

    def test_reset_nonzero_duration(self):
        timer = CountupTimer()
        timer.start()
        timer.reset(pytest.DURATION)
        assert timer._time_started is None
        assert timer._time_paused is None
        assert timer._elapsed == 0
        assert timer._duration == pytest.DURATION
        assert timer.paused is True
        assert timer.running is False

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
        time.sleep(pytest.SLEEPER)
        timer.resume()
        assert timer._time_started > start
        assert math.isclose(timer.elapsed, 0.0, abs_tol=pytest.ABS_TOL)
        assert timer.paused is False
        assert timer.running is True
        time.sleep(0.1)
        assert math.isclose(timer.elapsed, 0.1, rel_tol=pytest.REL_TOL)

    def test_resume_twice(self):
        start = time.time()
        timer = CountupTimer()
        timer.start()
        timer.pause()
        timer.resume()
        timer.resume()
        assert timer._time_started > start
        assert math.isclose(timer.elapsed, 0.0, abs_tol=pytest.ABS_TOL)
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
        time.sleep(pytest.SLEEPER)
        assert math.isclose(timer.elapsed, pytest.SLEEPER, rel_tol=pytest.REL_TOL)

    def test_get(self):
        timer = CountupTimer()
        timer.start()
        time.sleep(pytest.SLEEPER)
        got = timer._get()
        assert got > pytest.SLEEPER

    def test_get_with_pause(self):
        timer = CountupTimer()
        timer.start()
        time.sleep(pytest.SLEEPER)
        timer.pause()
        time.sleep(pytest.SLEEPER)
        got = timer._get()
        assert math.isclose(got, pytest.SLEEPER, rel_tol=pytest.REL_TOL)

    def test_get_not_started(self):
        timer = CountupTimer()
        got = timer._get()
        assert got == 0

    def test_expired(self):
        timer = CountupTimer(duration=pytest.DURATION)
        timer.start()
        assert timer.expired is False
        time.sleep(pytest.SLEEPER + pytest.DURATION)
        assert timer.expired is True

    def test_remaining(self):
        timer = CountupTimer(duration=pytest.DURATION)
        timer.start()
        assert math.isclose(timer.remaining, pytest.DURATION, rel_tol=pytest.REL_TOL)
        time.sleep(pytest.SLEEPER)
        assert math.isclose(
            timer.remaining, pytest.DURATION - pytest.SLEEPER, rel_tol=pytest.REL_TOL
        )


@pytest.mark.unit
class TestCountdownTimer:
    def test_start(self):
        timer = CountdownTimer(duration=pytest.DURATION)
        timer.start()
        assert timer._time_started is not None
        assert timer.paused is False

    def test_expired(self):
        timer = CountdownTimer(duration=pytest.DURATION)
        timer.start()
        assert timer.expired is False
        assert math.isclose(timer.remaining, pytest.DURATION, rel_tol=pytest.REL_TOL)
        time.sleep(pytest.DURATION + 0.1)  # just barely go beyond the duration
        assert timer.expired is True
        assert timer.remaining == 0

    def test_remaining(self):
        timer = CountdownTimer(duration=pytest.DURATION)
        timer.start()
        assert timer.expired is False
        time.sleep(pytest.SLEEPER)
        assert math.isclose(
            timer.remaining, pytest.DURATION - pytest.SLEEPER, rel_tol=pytest.REL_TOL
        )
        time.sleep(pytest.SLEEPER)
        assert math.isclose(
            timer.remaining,
            pytest.DURATION - (2 * pytest.SLEEPER),
            rel_tol=pytest.REL_TOL,
        )
        time.sleep(pytest.SLEEPER)
        assert math.isclose(
            timer.remaining,
            pytest.DURATION - (3 * pytest.SLEEPER),
            rel_tol=pytest.REL_TOL,
        )

    def test_pause(self):
        timer = CountdownTimer(duration=pytest.DURATION)
        timer.start()
        timer.pause()
        assert timer._time_paused is not None
        assert timer.paused is True
        assert timer.running is False
        assert timer._time_started is not None
        assert timer._time_paused > timer._time_started

    def test_resume(self):
        start = time.time()
        timer = CountdownTimer(duration=pytest.DURATION)
        timer.start()
        timer.pause()
        time.sleep(pytest.SLEEPER)
        timer.resume()
        assert timer._time_started > start
        assert math.isclose(timer.elapsed, 0, abs_tol=pytest.ABS_TOL)
        assert timer.paused is False
        assert timer.running is True
