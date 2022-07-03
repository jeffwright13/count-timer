from datetime import datetime, timedelta

class CountupTimer:
    def __init__(self):
        self.time_started = None
        self.time_paused = None
        self.paused = True

    def reset(self):
        self.__init__()

    def start(self):
        if self.time_started:
            return
        self.time_started = datetime.now()
        self.paused = False

    def pause(self):
        if self.paused or self.time_started is None:
            return
        self.time_paused = datetime.now()
        self.paused = True

    def resume(self):
        if not self.paused or self.time_started is None:
            return
        pause_time = datetime.now() - self.time_paused
        self.time_started = self.time_started + pause_time
        self.paused = False

    def get(self) -> timedelta:
        if not self.time_started:
            return None
        if self.paused:
            return self.time_paused - self.time_started
        else:
            return datetime.now() - self.time_started

    @property
    def elapsed(self) -> float:
        got = self.get()
        return got / timedelta(seconds=1) if got else 0


class CountupTimerWithExpiry(CountupTimer):
    def __init__(self, max_duration: float):
        super().__init__()
        self.max_duration = max_duration

    def reset(self):
        self.__init__(self.max_duration)

    @property
    def expired(self) -> bool:
        return self.elapsed >= self.max_duration


class CountdownTimerWithExpiry(CountupTimerWithExpiry):
    @property
    def time_left(self) -> float:
        got = self.get()
        return (
            self.max_duration - got / timedelta(seconds=1) if got else self.max_duration
        )
