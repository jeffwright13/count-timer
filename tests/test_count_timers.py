"""Define TestCountTimer class."""
# TODO: should these tests use the fixtures?


import math
import time

import pytest

from count_timer.count_timer import CountTimer


class TestCountTimer:
    """Class to encapsulate methods for testing CountTimer."""

    def test_init(self, count_timer_zero_duration):
        """Default instance-variable values set correctly."""
        timer = CountTimer()
        assert timer._time_started is None
        assert timer._time_paused is None
        assert timer._elapsed == 0
        assert timer._duration == 0
        assert timer.paused is True
        assert timer.running is False

    def test_init_nonzero_duration(self):
        """Constructor understands duration parameter."""
        timer = CountTimer(duration=pytest.DURATION)
        assert timer._time_started is None
        assert timer._time_paused is None
        assert timer._elapsed == 0
        assert timer._duration == pytest.DURATION
        assert timer.paused is True
        assert timer.running is False

    def test_start(self):
        """start() starts timer."""
        timer = CountTimer(duration=pytest.DURATION)
        timer.start()
        assert timer._time_started is not None
        assert timer.paused is False

    def test_reset(self):
        """reset() resets timer to default value of 0."""
        timer = CountTimer()
        timer.start()
        timer.reset()
        assert timer._time_started is None
        assert timer._time_paused is None
        assert timer._elapsed == 0
        assert timer._duration == 0
        assert timer.paused is True
        assert timer.running is False

    def test_reset_nonzero_duration(self):
        """reset() resets timer to passed value."""
        timer = CountTimer()
        timer.start()
        timer.reset(pytest.DURATION)
        assert timer._time_started is None
        assert timer._time_paused is None
        assert timer._elapsed == 0
        assert timer._duration == pytest.DURATION
        assert timer.paused is True
        assert timer.running is False

    def test_start_twice(self):
        """Second start() calls allowed."""
        timer = CountTimer()
        timer.start()
        timer.start()
        assert timer._time_started is not None
        assert timer.paused is False

    def test_pause(self):
        """pause() pauses timer execution."""
        timer = CountTimer()
        timer.start()
        timer.pause()
        assert timer._time_paused is not None
        assert timer.paused is True
        assert timer.running is False
        assert timer._time_started is not None
        assert timer._time_paused > timer._time_started

    def test_pause_twice(self):
        """pause() while paused is legal."""
        timer = CountTimer()
        timer.start()
        timer.pause()
        timer.pause()
        assert timer._time_paused is not None
        assert timer.paused is True
        assert timer.running is False

    def test_pause_while_not_started(self):
        """pause() before starting is legal."""
        timer = CountTimer()
        timer.pause()
        assert timer._time_paused is None
        assert timer.paused is True
        assert timer.running is False

    def test_resume(self):
        """resume() resumes a paused timer."""
        start = time.time()
        timer = CountTimer()
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
        """No effect of resume() on a resumed timer."""
        start = time.time()
        timer = CountTimer()
        timer.start()
        timer.pause()
        timer.resume()
        timer.resume()
        assert timer._time_started > start
        assert math.isclose(timer.elapsed, 0.0, abs_tol=pytest.ABS_TOL)
        assert timer.paused is False
        assert timer.running is True

    def test_resume_not_started(self):
        """No effect of resume() on a timer that's never been started."""
        timer = CountTimer()
        timer.resume()
        assert timer._time_started is None
        assert timer.paused is True

    def test_elapsed(self):
        """The elapsed property tracks elapsed time correctly."""
        timer = CountTimer()
        timer.start()
        time.sleep(pytest.SLEEPER)
        assert math.isclose(timer.elapsed, pytest.SLEEPER, rel_tol=pytest.REL_TOL)

    def test_get(self):
        """_get() gets elapsed time for running timer."""
        timer = CountTimer()
        timer.start()
        time.sleep(pytest.SLEEPER)
        got = timer._get()
        assert got > pytest.SLEEPER

    def test_get_with_pause(self):
        """_get() does not count time paused."""
        timer = CountTimer()
        timer.start()
        time.sleep(pytest.SLEEPER)
        timer.pause()
        time.sleep(pytest.SLEEPER)
        got = timer._get()
        assert math.isclose(got, pytest.SLEEPER, rel_tol=pytest.REL_TOL)

    def test_get_not_started(self):
        """_get() returns 0 before timer is started."""
        timer = CountTimer()
        got = timer._get()
        assert got == 0

    def test_expired(self):
        """The expired property reports whether the timer has expired."""
        timer = CountTimer(duration=pytest.DURATION)
        timer.start()
        assert timer.expired is False
        time.sleep(pytest.SLEEPER + pytest.DURATION)
        assert timer.expired is True

    def test_remaining_1(self):
        """The remaining property reports the time remaining to run."""
        timer = CountTimer(duration=pytest.DURATION)
        timer.start()
        assert math.isclose(timer.remaining, pytest.DURATION, rel_tol=pytest.REL_TOL)
        time.sleep(pytest.SLEEPER)
        assert math.isclose(
            timer.remaining, pytest.DURATION - pytest.SLEEPER, rel_tol=pytest.REL_TOL
        )

    def test_remaining_2(self):
        """Check remaining time several times in succession."""
        timer = CountTimer(duration=pytest.DURATION)
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

    def test_start_2(self):
        """A started timer knows it's started and not paused."""
        timer = CountTimer(duration=pytest.DURATION)
        timer.start()
        assert timer._time_started is not None
        assert timer.paused is False

    def test_expired_2(self):
        """A timer expires immediately after its duration."""
        timer = CountTimer(duration=pytest.DURATION)
        timer.start()
        assert timer.expired is False
        assert math.isclose(timer.remaining, pytest.DURATION, rel_tol=pytest.REL_TOL)
        time.sleep(pytest.DURATION + 0.1)  # just barely go beyond the duration
        assert timer.expired is True
        assert timer.remaining == 0

    def test_pause_2(self):
        """A paused timer is paused after it is started."""
        timer = CountTimer(duration=pytest.DURATION)
        timer.start()
        timer.pause()
        assert timer._time_paused is not None
        assert timer.paused is True
        assert timer.running is False
        assert timer._time_started is not None
        assert timer._time_paused > timer._time_started

    def test_resume_2(self):
        """A paused timer does not accumulate time."""
        start = time.time()
        timer = CountTimer(duration=pytest.DURATION)
        timer.start()
        timer.pause()
        time.sleep(pytest.SLEEPER)
        timer.resume()
        assert timer._time_started > start
        assert math.isclose(timer.elapsed, 0, abs_tol=pytest.ABS_TOL)
        assert timer.paused is False
        assert timer.running is True

    # new from here down
    def test_pause_bad_object(self):
        """A badly initialized timer does not pause correctly."""
        timer = CountTimer()
        assert timer._paused
        assert not timer._time_paused
        timer._paused = False  # make the object bad
        assert not timer._paused
        assert not timer._time_paused
        timer.pause()
        assert not timer._paused
        assert not timer._time_paused
        # now reverse it
        timer = CountTimer()
        assert timer._paused
        assert not timer._time_paused
        timer._time_paused = 1  # make the object bad
        assert timer._paused
        assert timer._time_paused
        timer.pause()
        assert timer._paused
        assert timer._time_paused

    def test_duration_property(self):
        """The duration property reports the duration time requested."""
        timer = CountTimer(duration=pytest.DURATION)
        assert timer.duration == pytest.DURATION

    def test_exactly_expired(self):
        """A timer paused exactly at the end of the duration is, nonetheless, expaired."""
        timer = CountTimer(duration=pytest.DURATION)
        timer.start()
        timer.pause()
        timer._time_paused = timer._time_started + timer._duration
        assert timer.expired

    def test_no_time_elapsed_until_timer_started(self):
        """No time elapses unless the timer is started."""
        timer = CountTimer(duration=pytest.DURATION)
        time.sleep(pytest.SLEEPER)
        assert timer.elapsed == 0
