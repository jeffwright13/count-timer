from datetime import datetime, timedelta

class CountupTimer:
    def __init__(self):
        self._time_started = None
        self._time_paused = None
        self._paused = True

    def reset(self):
        self.__init__()

    def start(self):
        if self._time_started:
            return
        self._time_started = datetime.now()
        self._paused = False

    def pause(self):
        if self._paused or self._time_started is None:
            return
        self._time_paused = datetime.now()
        self._paused = True

    def resume(self):
        if not self._paused or self._time_started is None:
            return
        pause_time = datetime.now() - self._time_paused
        self._time_started = self._time_started + pause_time
        self._paused = False

    def get(self) -> timedelta:
        if not self._time_started:
            return None
        if self._paused:
            return self._time_paused - self._time_started
        else:
            return datetime.now() - self._time_started

    @property
    def paused(self) -> bool:
        return self._paused

    @property
    def elapsed(self) -> float:
        got = self.get()
        return got / timedelta(seconds=1) if got else 0


class CountupTimerWithExpiry(CountupTimer):
    def __init__(self, duration: float):
        super().__init__()
        self._duration = duration

    def reset(self):
        self.__init__(self._duration)

    @property
    def expired(self) -> bool:
        return self.elapsed >= self._duration


class CountdownTimerWithExpiry(CountupTimerWithExpiry):
    @property
    def time_left(self) -> float:
        got = self.get()
        return (
            self._duration - got / timedelta(seconds=1) if got else self._duration
        )
