# counters
A collection of counters of various types for general use

---
**CountupTimer()**

```
╭─ <class 'counters.counters.CountupTimer'> ─╮
│ class CountupTimer():                      │
│                                            │
│ elapsed = <property object at 0x1068a1e00> │
│  paused = <property object at 0x106885d60> │
╰────────────────────────────────────────────╯
```
***elapsed:***
float
Time (fractional seconds) since the timer was started

***paused:***
bool
Whether or not the timer's countup has been paused

---
**CountupTimerWithExpiry(duration: float)**

```
╭─ <class 'counters.counters.CountupTimerWithExpiry'> ─╮
│ class CountupTimerWithExpiry(duration: float):       │
│                                                      │
│ elapsed = <property object at 0x1068a1e00>           │
│  paused = <property object at 0x106885d60>           │
│ expired = <property object at 0x1068a1ef0>           │
╰──────────────────────────────────────────────────────╯
```
***elapsed:***
float
Time (fractional seconds) since the timer was started

***paused:***
bool
Whether or not the timer's countup has been paused

***expired:***
bool
Whether or not the timer's configured expiration value has been exceeded

---
**CountdownTimerWithExpiry(duration: float)**

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
│       get = def get(self) -> datetime.timedelta:       │
╰────────────────────────────────────────────────────────╯
```

## CountdownTimerWithExpiry(duration: float)
Creates a countdown timer, with configurable countdown duration (fractional seconds). The timer starts at time `t=duration`, and counts down using the system clock until it hits `t=0`. At that time, the `expired` property is set to `True`.

The clock can be paused while counting down, using the `pause()` method. When paused, the countdown timer stops its descent towards `t=0`. When the clock is resumed again (using the `resume()` method), the countdown continues from where it left off.

***elapsed:***
float
Time (fractional seconds) since the timer was started

***paused:***
bool
Whether or not the timer's countdown has been paused

***expired:***
bool
Whether or not the timer has counted down from its configured max to zero (0)

***time_left:***
float
Time (fractional seconds) until the timer expires

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
