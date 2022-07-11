# counters
A counting-up and a counting-down timer with nanosecond precision

---
## CountupTimer(duration: float)
Creates a countup timer, with configurable expiration time (seconds). The timer starts at time `t=0`, and counts up using the system clock until it hits `t=duration`. At that time, the `expired` property is set to `True`. Note that the counter continues incrementing beyond the expiration time.

The clock can be paused using the `pause()` method. When paused, the countup timer stops incrementing. When the clock is resumed again (using the `resume()` method), it continues from where it left off.

```
╭───────── <class 'counters.counters.CountupTimer'> ─────────╮
│ A timer that can be started, paused, resumed and reset.    │
│                                                            │
│ Invocation: CountupTimer(duration=0)                       |
│                                                            │
│ ╭────────────────────────────────────────────────────────╮ │
│ │ <counters.counters.CountupTimer object at 0x111d4ec10> │ │
│ ╰────────────────────────────────────────────────────────╯ │
│                                                            │
│  duration = 0                                              │
│   elapsed = 0                                              │
│   expired = True                                           │
│    paused = True                                           │
│ remaining = 0                                              │
│   running = False                                          │
╰────────────────────────────────────────────────────────────╯
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

---
## CountdownTimer(duration: float)
Creates a countdown timer, with configurable countdown duration (seconds). The timer starts at time `t=duration`, and counts down using the system clock until it hits `t=0`. At that time, the `expired` property is set to `True`. Note that the counter continues incrementing beyond the execution time.

The clock can be paused while counting down, using the `pause()` method. When paused, the countdown timer stops its descent towards `t=0`. When the clock is resumed again (using the `resume()` method), the countdown continues from where it left off.

```
╭───────── <class 'counters.counters.CountdownTimer'> ─────────╮
│ ╭──────────────────────────────────────────────────────────╮ │
│ │ <counters.counters.CountdownTimer object at 0x1120361f0> │ │
│ ╰──────────────────────────────────────────────────────────╯ │
│                                                              │
│ Invocation: CountdownTimer(duration=0)                       |
│                                                              │
│  duration = 0                                                │
│   elapsed = 0                                                │
│   expired = True                                             │
│    paused = True                                             │
│ remaining = 0                                                │
│   running = False                                            │
╰──────────────────────────────────────────────────────────────╯
```

***elapsed:***
float
Time (seconds) since the timer was started

***paused:***
bool
Whether or not the timer's countdown has been paused

***expired:***
bool
Whether or not the timer has counted down from its configured max to zero (0)

***time_left:***
float
Time (seconds) until the timer expires

***start():***
start() -> None
Starts the timer, counting down backwards from the configured duration to zero (0)

***pause():***
pause() -> None
Pauses the timer - when the timer is paused, the countdown is stopped until resumed

***resume():***
resume() -> None
Resumes / unpauses the timer - when the timer is resumed, the countdown starts from where it was when paused

***reset():***
reset() -> None
Puts the timer back in its original state when first created (paused / not yet started)
