import re
import time

import keyboard
import pygetwindow as pg


def wait_windows(name_like: str, timeout=5):
    is_win_activate = False
    time_sleep = 0.1
    max_sec = int(round(timeout / time_sleep))
    n = 0
    while is_win_activate is False:
        if n > max_sec:
            print('Time')
            break
        try:
            if re.search(name_like, pg.getActiveWindow().title):
                return True
        except AttributeError:
            pass
        time.sleep(time_sleep)
        n += 1

        if n % 10 == 0:
            print(f'Wait window like [{name_like}] in {pg.getAllTitles()}')
        # print(pg.getAllTitles())
        for window in pg.getAllTitles():
            if re.search(name_like, window):
                is_win_activate = True
                try:
                    pg.getWindowsWithTitle(window)[0].activate()
                    return True
                except Exception:
                    continue
            time.sleep(0.1)
    raise Exception('Timeout')


def window_fullscreen():
    keyboard.press_and_release('win + up')
