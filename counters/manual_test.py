import time
from datetime import datetime
from rich import inspect
from counters import CountupTimer, CountupTimerWithExpiry, CountdownTimer


def test_countupexpiry_inspect(iterations: int = 10, duration: int = 0.75):
    countup_timer = CountupTimerWithExpiry(duration)
    countup_timer.start()

    for _ in range(iterations):
        print(inspect(countup_timer))
        time.sleep(duration)

    countup_timer.pause()
    inspect(countup_timer)
    time.sleep(2)
    countup_timer.resume()

    for _ in range(iterations):
        inspect(countup_timer)
        time.sleep(duration)


def test_countupexpiry_print(iterations: int = 10, duration: int = 0.75):
    countup_timer = CountupTimerWithExpiry(duration)
    countup_timer.start()

    print("Now\t\tElapsed\t\tPaused")
    for _ in range(8):
        print(
            f"{round(datetime.now().second,0)}\t\t{round(countup_timer.elapsed, 3)}\t\t{countup_timer.paused}",
            end="\r",
        )
        time.sleep(1)
    countup_timer.pause()
    for _ in range(8):
        print(
            f"{datetime.now().second}\t\t{round(countup_timer.elapsed, 3)}\t\t{countup_timer.paused}",
            end="\r",
        )
        time.sleep(1)
    countup_timer.resume()
    for _ in range(8):
        print(
            f"{datetime.now().second}\t\t{round(countup_timer.elapsed, 3)}\t\t{countup_timer.paused}",
            end="\r",
        )
        time.sleep(1)
    print("")


def main():
    # test_countupexpiry_inspect(10)
    test_countupexpiry_print(10)


if __name__ == "__main__":
    main()
