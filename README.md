# count-timer

A class implementing a counting-up/counting-down timer

## Installation
`$ pip install count-timer`

## Demo
This is a rudimentary text-based demonstration of the count-down version of the CountTimer class. You can launch it directly:

`$ demo`

...or from Python:

`$ python count_timer/demo_async.py`

Once launched, the demo will prompt you to enter a duration (the count-down timer expiration value). The timer will begin counting down on the terminal. The time will transition to yellow when there is <10 sec before expiration, and red when there are <5 sec.

Pressing "q" will cause the timer to quit.

Pressing "r" will cause the timer to restart at the original duration.

The timer may be paused/resumed by pressing the space bar.


## API

### CountTimer(duration: float)
Creates a counting timer, with configurable duration (seconds). The timer starts at time `t=0`, and counts up using the system clock until it hits `t=duration`. At that time, the `expired` property is set to `True`. Note that the counter continues incrementing beyond the expiration time.

If `duration` is set to zero (which is the default), the timer never expires and continues to count forever.

The timer can be paused using the `pause()` method. When paused, the timer stops incrementing. When the clock is resumed again (using the `resume()` method), it continues from where it left off.

This counter/timer can be used as a "count-up" timer or a "count-down" timer. The default mode of interpretation is "up," but if you prefer a countdown time, simply look at the `remaining` property instead of `elapsed`.

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                      count_timer.count_timer.CountTimer                             │
└─────────────────────────────────────────────────────────────────────────────────────┘
class CountTimer(duration=0):
    A counting timer (w/ optional expiry that can be started, paused, resumed and reset

    Configuration:
        duration: Number of seconds to elapse before expiration
                  (optional; default: 0 - indicates time never expires)

    Methods:
        start(): start the timer
        pause(): pause the timer
        resume(): resume the timer
        reset(): reset the timer to default (duration 0/paused/not started)

    Properties:
        paused: True if timer is paused
        running: True if timer is running
        duration: value of the 'duration' config param
        elapsed: time (sec) since timer was started
        remaining: time (sec) until timer expires

    Inspiration from https://stackoverflow.com/a/60027719/4402572

   def start(self):
       Start the timer.
   def pause(self):
       Pause the timer.
   def resume(self):
       Resume the timer.
   def reset(self, duration=0):
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
