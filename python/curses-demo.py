import curses
import time
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.addstr(10,10,"Hello World")
screen.refresh()
time.sleep(5)
curses.endwin()