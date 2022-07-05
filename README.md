# counters
A collection of counters of various types for general use

---
## CountupTimer()
Creates a no-frills counting-up timer. The timer starts at zero time (`t=0`), and counts up using the system clock indefinitely.

The clock can be paused by using the `pause()` method. When paused, the count-up timer stops its ascent. When the clock is resumed again (using the `resume()` method), the count continues upwards from where it left off.

```
╭──── <class 'counters.counters.CountupTimer'> ──────╮
│ class CountupTimer():                              │
│                                                    │
│ elapsed = <property object at 0x1068a1e00>         │
│  paused = <property object at 0x106885d60>         │
|                                                    |
| methods:                                           |
│     start = def start(self):                       │
│     pause = def pause(self):                       │
│    resume = def resume(self):                      │
│     reset = def reset(self):                       │
│       get = def get(self) -> datetime.timedelta:   │
╰────────────────────────────────────────────────────╯
```

***elapsed:***
float
Time (seconds) since the timer was started

***paused:***
bool
Whether or not the timer's countup has been paused

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

***get():***
get(self) -> datetime.timedelta
Returns the elapsed running time (not including pauses) since the timer was started or reset

---
## CountupTimerWithExpiry(duration: float)
Creates a countup timer, with configurable expiration time (seconds). The timer starts at time `t=0`, and counts up using the system clock until it hits `t=duration`. At that time, the `expired` property is set to `True`.

The clock can be paused using the `pause()` method. When paused, the countup timer stops its ascent towards `t=duration`. When the clock is resumed again (using the `resume()` method), it continues from where it left off.

```
╭─ <class 'counters.counters.CountupTimerWithExpiry'> ─╮
│ class CountupTimerWithExpiry(duration: float):       │
│                                                      │
│ elapsed = <property object at 0x1068a1e00>           │
│  paused = <property object at 0x106885d60>           │
│ expired = <property object at 0x1068a1ef0>           │
|                                                      |
| methods:                                             |
│     start = def start(self):                         │
│     pause = def pause(self):                         │
│    resume = def resume(self):                        │
│     reset = def reset(self):                         │
│       get = def get(self) -> datetime.timedelta      │
╰──────────────────────────────────────────────────────╯
```

***elapsed:***
float
Time (seconds) since the timer was started

***paused:***
bool
Whether or not the timer's countup has been paused

***expired:***
bool
Whether or not the timer's configured expiration value has been exceeded

---
## CountdownTimerWithExpiry(duration: float)
Creates a countdown timer, with configurable countdown duration (seconds). The timer starts at time `t=duration`, and counts down using the system clock until it hits `t=0`. At that time, the `expired` property is set to `True`.

The clock can be paused while counting down, using the `pause()` method. When paused, the countdown timer stops its descent towards `t=0`. When the clock is resumed again (using the `resume()` method), the countdown continues from where it left off.

```
╭─ <class 'counters.counters.CountdownTimerWithExpiry'> ─╮
│ class CountdownTimerWithExpiry(duration: float):       │
│                                                        │
│ properties:                                            │
│   elapsed = <property object at 0x1068a1e00>           │
│    paused = <property object at 0x106885d60>           │
│   expired = <property object at 0x1068a1ef0>           │
│ time_left = <property object at 0x1068a1f90>           │
|                                                        |
| methods:                                               |
│     start = def start(self):                           │
│     pause = def pause(self):                           │
│    resume = def resume(self):                          │
│     reset = def reset(self):                           │
│       get = def get(self) -> datetime.timedelta        │
╰────────────────────────────────────────────────────────╯
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

***get():***
get(self) -> datetime.timedelta
Returns the elapsed running time (not including pauses) since the timer was started or reset
