import sys
import asyncio
from count_timer import CountTimer
from blessed import Terminal


def count():
    if counter.remaining > 10:
        print(
            term.bold
            + term.green
            + term.move_x(0)
            + term.move_up
            + term.clear_eol
            + str(round(counter.remaining, 3))
        )
    elif counter.remaining > 5:
        print(
            term.bold
            + term.yellow2
            + term.move_x(0)
            + term.move_up
            + term.clear_eol
            + str(round(counter.remaining, 3))
        )
    elif counter.remaining > 0:
        print(
            term.bold
            + term.red
            + term.move_x(0)
            + term.move_up
            + term.clear_eol
            + str(round(counter.remaining, 3))
        )
    else:
        print(
            term.bold
            + term.magenta
            + term.move_x(0)
            + term.move_up
            + term.clear_eol
            + "TIME'S UP!"
        )


def kb_input():
    if counter.remaining <= 0:
        return
    with term.cbreak():
        key = term.inkey(timeout=0.01).lower()
        if key:
            if key == "q":
                print(
                    term.bold
                    + term.magenta
                    + term.move_x(0)
                    + term.move_up
                    + term.clear_eol
                    + "Quitting..."
                )
                sys.exit()
            elif key == "r":
                counter.reset(duration=float(duration))
                counter.start()
            elif key == " ":
                counter.pause() if counter.running else counter.resume()


async def main():
    global counter
    global term
    global duration

    duration = input("Enter countdown timer duration: ")
    counter = CountTimer(duration=float(duration))
    counter.start()
    term = Terminal()

    def _run_executor_count():
        count()

    def _run_executor_kb_input():
        kb_input()

    while counter.remaining > 0:
        await asyncio.get_event_loop().run_in_executor(None, _run_executor_count)
        await asyncio.get_event_loop().run_in_executor(None, _run_executor_kb_input)

    await asyncio.get_event_loop().run_in_executor(None, _run_executor_count)


def async_main_entry():
    asyncio.get_event_loop().run_until_complete(main())


if __name__ == "__main__":
    async_main_entry()
