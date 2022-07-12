# counters
A counting-up and a counting-down timer with nanosecond precision

---
## CountTimer(duration: float)
Creates a counting timer, with configurable duration (seconds). The timer starts at time `t=0`, and counts up using the system clock until it hits `t=duration`. At that time, the `expired` property is set to `True`. Note that the counter continues incrementing beyond the expiration time.

If `duration` is set to zero (which is the default), the timer never expires and continues to count forever.

The timer can be paused using the `pause()` method. When paused, the timer stops incrementing. When the clock is resumed again (using the `resume()` method), it continues from where it left off.

This counter/timer can be used as a "count-up" timer or a "count-down" timer. The default mode of interpretation is "up," but if you prefer a countdown time, simply look at the `remaining` property instead of `elapsed`.

```
╭───────── <class 'counters.counters.CountupTimer'> ─────────────────────╮
│ A counting- timer that can be started, paused, resumed and reset.      │
│                                                                        │
│ ╭────────────────────────────────────────────────────────╮             │
│ │ <counters.counters.CountTimer object at 0x111d4ec10>   │             │
│ ╰────────────────────────────────────────────────────────╯             │
│                                                                        │
│ Invocation: CountTimer(duration=0)                                     |
│                                                                        │
│  duration = 0                                                          │
│   elapsed = 0                                                          │
│   expired = True                                                       │
│    paused = True                                                       │
│ remaining = 0                                                          │
│   running = False                                                      │
╰────────────────────────────────────────────────────────────────────────╯
```

***elapsed:***
float
Time (seconds) since the timer was started

***paused:***
bool
Whether or not the timer's countup has been paused

***running:***
bool
Whether or not the timer is currently running (i.e. incrementing internally)

***expired:***
bool
Whether or not the timer's configured expiration value has been exceeded

***start():***
start() -> None
Starts the timer, counting up indefinitely

***pause():***
pause() -> None
Pauses the timer; the countup is stopped until resumed

***resume():***
resume() -> None
Resumes / unpauses the timer - when the timer is resumed, the countdown starts from where it was when paused

***reset():***
reset() -> None
Puts the timer back in its original state when first created (paused / not yet started)
