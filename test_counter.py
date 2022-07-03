import pytest
import math
import time
from datetime import datetime
from counter import CountupTimer, CountupTimerWithExpiry, CountdownTimerWithExpiry
from datetime import timezone

class TestCountupTimer:
    def test_start(self):
        timer = CountupTimer()
        timer.start()
        assert timer.time_started is not None
        assert timer.paused is False

    def test_reset(self):
        timer = CountupTimer()
        timer.start()
        timer.reset()
        assert timer.time_started is None
        assert timer.time_paused is None
        assert timer.paused is True

    def test_start_twice(self):
        timer = CountupTimer()
        timer.start()
        timer.start()
        assert timer.time_started is not None
        assert timer.paused is False

    def test_pause(self):
        timer = CountupTimer()
        timer.start()
        timer.pause()
        assert timer.time_paused is not None
        assert timer.paused is True

    def test_pause_twice(self):
        timer = CountupTimer()
        timer.start()
        timer.pause()
        timer.pause()
        assert timer.time_paused is not None
        assert timer.paused is True

    def test_resume(self):
        start = datetime.now()
        timer = CountupTimer()
        timer.start()
        timer.pause()
        timer.resume()
        assert timer.time_started > start
        assert timer.paused is False

    def test_resume_twice(self):
        start = datetime.now()
        timer = CountupTimer()
        timer.start()
        timer.pause()
        timer.resume()
        timer.resume()
        assert timer.time_started > start
        assert timer.paused is False

    def test_elapsed(self):
        timer = CountupTimer()
        timer.start()
        time.sleep(0.5)
        assert math.isclose(timer.elapsed, 0.5, rel_tol=0.01)

class TestCountupTimerWithExpiry:
    def test_start(self):
        timer = CountupTimerWithExpiry(max_duration=1)
        timer.start()
        assert timer.time_started is not None
        assert timer.paused is False

    def test_expired(self):
        timer = CountupTimerWithExpiry(max_duration=0.5)
        timer.start()
        assert timer.expired is False
        time.sleep(0.51)
        assert timer.expired is True

class TestCountdownTimerWithExpiry:
    def test_start(self):
        timer = CountdownTimerWithExpiry(max_duration=1)
        timer.start()
        assert timer.time_started is not None
        assert timer.paused is False

    def test_expired(self):
        timer = CountdownTimerWithExpiry(max_duration=1)
        timer.start()
        assert timer.expired is False
        assert timer.time_left > 0
        time.sleep(1.01)
        assert timer.expired is True
        assert timer.time_left <= 0
