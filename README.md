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
│   elapsed = <property object at 0x1068a1e00>           │
│    paused = <property object at 0x106885d60>           │
│   expired = <property object at 0x1068a1ef0>           │
│ time_left = <property object at 0x1068a1f90>           │
╰────────────────────────────────────────────────────────╯
```
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
