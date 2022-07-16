import sys
from threading import Thread
from count_timer import CountTimer
from blessed import Terminal


def count():
    # global counter
    # global term
    term.clear()

    while counter.remaining > 0:
        if counter.remaining > 10:
            print(
                term.bold
                + term.green
                + term.move_x(0)
                + term.move_up
                + term.clear_eol
                + str(round(counter.remaining, 3))
            )
            continue

        if counter.remaining > 5:
            print(
                term.bold
                + term.yellow
                + term.move_x(0)
                + term.move_up
                + term.clear_eol
                + str(round(counter.remaining, 3))
            )
            continue

        if counter.remaining > 0:
            print(
                term.bold
                + term.red
                + term.move_x(0)
                + term.move_up
                + term.clear_eol
                + str(round(counter.remaining, 3))
            )
            continue

    print(
        term.bold
        + term.magenta
        + term.move_x(0)
        + term.move_up
        + term.clear_eol
        + "TIME'S UP!"
    )
    term.clear()
    print(term.normal)


def take_input():
    while counter.remaining > 0:
        with term.cbreak():
            key = term.inkey()
            if key == "q":
                sys.exit()
            counter.pause() if counter.running else counter.resume()


def main():
    global counter
    global term

    duration = input("Enter countdown timer duration: ")
    counter = CountTimer(duration=float(duration))
    counter.start()
    term = Terminal()
    term.clear()

    t1 = Thread(target=count)
    t2 = Thread(target=take_input)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
