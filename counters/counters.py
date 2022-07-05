from datetime import datetime

class CountupTimer:
    """
    A timer that can be started, paused, resumed and reset.

    Start: starts the timer
    Pause: pauses the timer
    Resume: resumes the timer
    Reset: Resets the timer to 0/paused/not started

    Inspiration from https://stackoverflow.com/a/60027719/4402572
    """
    def __init__(self):
        """Create a new timer."""
        self._time_started = None
        self._time_paused = None
        self._elapsed = 0
        self._paused = True

    def reset(self):
        self.__init__()

    def start(self):
        """Start the timer."""
        if self._time_started:
            return
        self._time_started = datetime.now().timestamp()
        self._paused = False

    def pause(self):
        """Pause the timer."""
        if self._paused or self._time_started is None:
            return
        self._time_paused = datetime.now().timestamp()
        self._paused = True

    def resume(self):
        """Resume the timer."""
        if not self._paused or self._time_started is None:
            return
        pause_duration = datetime.now().timestamp() - self._time_paused
        self._time_started = self._time_started + pause_duration
        self._paused = False

    def _get(self) -> float:
        """Time in sec since timer was started, minus any time paused."""
        if not self._time_started:
            return 0
        if self._paused:
            return self._time_paused - self._time_started
        else:
            return datetime.now().timestamp() - self._time_started

    @property
    def paused(self) -> bool:
        """True if the timer is paused, False if not."""
        return self._paused

    @property
    def running(self) -> bool:
        """False if the timer is paused, True if not."""
        return not self._paused

    @property
    def elapsed(self) -> float:
        """Time elapsed (seconds) since timer was started, minus time paused."""
        got = self._get()
        return got or 0


class CountupTimerWithExpiry(CountupTimer):
    def __init__(self, duration: float):
        """Create a new timer."""
        super().__init__()
        self._duration = duration

    def reset(self):
        """Reset the timer."""
        self.__init__(self._duration)

    @property
    def duration(self) -> bool:
        """Timer's configured expiry value."""
        return self._duration

    @property
    def expired(self) -> bool:
        """True if the timer has expired, False if not."""
        return self.elapsed >= self._duration

    @property
    def remaining(self) -> float:
        """Time left (in seconds) until the timer expires."""
        got = self._get()
        time_left = self._duration - got
        return time_left if time_left <= self.duration else 0

class CountdownTimerWithExpiry(CountupTimerWithExpiry):
    @property
    def remaining(self) -> float:
        """Time left (in seconds) until the timer expires."""
        got = self._get()
        time_left = self._duration - got
        return time_left if time_left >= 0 else 0
