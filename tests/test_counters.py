import math
import pytest
import time
from datetime import datetime
from counters.counters import (
    CountupTimer,
    CountupTimerWithExpiry,
    CountdownTimerWithExpiry,
)


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
        start = datetime.now().timestamp()
        timer = CountupTimer()
        timer.start()
        timer.pause()
        timer.resume()
        assert timer._time_started > start
        assert timer.paused is False

    def test_resume_twice(self):
        start = datetime.now().timestamp()
        timer = CountupTimer()
        timer.start()
        timer.pause()
        timer.resume()
        timer.resume()
        assert timer._time_started > start
        assert timer.paused is False

    def test_resume_not_started(self):
        timer = CountupTimer()
        timer.resume()
        assert timer._time_started is None
        assert timer.paused is True

    def test_elapsed(self):
        sleep = 0.3
        timer = CountupTimer()
        timer.start()
        time.sleep(sleep)
        assert math.isclose(timer.elapsed, sleep, rel_tol=0.02)

    def test_get(self):
        sleep = 0.3
        timer = CountupTimer()
        timer.start()
        time.sleep(sleep)
        got = timer._get()
        assert got > sleep

    def test_get_with_pause(self):
        sleep1 = 0.3
        sleep2 = 0.2
        timer = CountupTimer()
        timer.start()
        time.sleep(sleep1)
        timer.pause()
        time.sleep(sleep2)
        got = timer._get()
        assert math.isclose(got, sleep1, rel_tol=0.2)

    def test_get_not_started(self):
        timer = CountupTimer()
        got = timer._get()
        assert got == 0


@pytest.mark.unit
class TestCountupTimerWithExpiry:
    def test_start(self):
        timer = CountupTimerWithExpiry(duration=1)
        timer.start()
        assert timer._time_started is not None
        assert timer.paused is False

    def test_expired(self):
        timer = CountupTimerWithExpiry(duration=0.5)
        timer.start()
        assert timer.expired is False
        time.sleep(0.51)
        assert timer.expired is True


@pytest.mark.unit
class TestCountdownTimerWithExpiry:
    def test_start(self):
        timer = CountdownTimerWithExpiry(duration=1)
        timer.start()
        assert timer._time_started is not None
        assert timer.paused is False

    def test_expired(self):
        timer = CountdownTimerWithExpiry(duration=1)
        timer.start()
        assert timer.expired is False
        assert timer.remaining > 0
        time.sleep(1.01)
        assert timer.expired is True
        assert timer.remaining <= 0

    def test_time_left(self):
        sleep = 1.01
        timer = CountdownTimerWithExpiry(duration=1)
        timer.start()
        assert timer.expired is False
        time.sleep(sleep)
        assert math.isclose(timer.remaining, 0, rel_tol=0.2)
        assert timer.expired is True
